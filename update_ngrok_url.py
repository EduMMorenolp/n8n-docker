#!/usr/bin/env python3
import requests
import os
import subprocess
import json
from datetime import datetime

def get_ngrok_url():
    """Obtiene la URL actual de ngrok"""
    try:
        response = requests.get('http://localhost:4040/api/tunnels', timeout=10)
        tunnels = response.json()['tunnels']
        
        for tunnel in tunnels:
            if tunnel['proto'] == 'https' and tunnel['config']['addr'] == 'n8n:5678':
                return tunnel['public_url']
        return None
    except Exception as e:
        print(f"Error obteniendo URL de ngrok: {e}")
        return None

def check_url_status(url):
    """Verifica si la URL está online"""
    try:
        response = requests.get(f"{url}/healthz", timeout=10)
        return response.status_code == 200
    except:
        return False

def update_env_file(new_url):
    """Actualiza el archivo .env con la nueva URL"""
    env_path = '/opt/n8n/.env'
    
    try:
        # Leer archivo actual
        with open(env_path, 'r') as f:
            lines = f.readlines()
        
        # Actualizar línea de webhook URL
        updated = False
        for i, line in enumerate(lines):
            if line.startswith('N8N_WEBHOOK_URL='):
                lines[i] = f'N8N_WEBHOOK_URL={new_url}\n'
                updated = True
                break
        
        if updated:
            # Escribir archivo actualizado
            with open(env_path, 'w') as f:
                f.writelines(lines)
            return True
        return False
    except Exception as e:
        print(f"Error actualizando .env: {e}")
        return False

def restart_n8n():
    """Reinicia el contenedor de n8n"""
    try:
        subprocess.run(['docker', 'restart', 'n8n-app'], check=True)
        return True
    except Exception as e:
        print(f"Error reiniciando n8n: {e}")
        return False

def main():
    """Función principal"""
    result = {
        'timestamp': datetime.now().isoformat(),
        'status': 'success',
        'message': '',
        'old_url': os.getenv('N8N_WEBHOOK_URL', ''),
        'new_url': '',
        'url_changed': False
    }
    
    # Obtener URL actual de ngrok
    current_ngrok_url = get_ngrok_url()
    if not current_ngrok_url:
        result['status'] = 'error'
        result['message'] = 'No se pudo obtener la URL de ngrok'
        print(json.dumps(result))
        return
    
    result['new_url'] = current_ngrok_url
    
    # Verificar si la URL actual está online
    current_env_url = os.getenv('N8N_WEBHOOK_URL', '')
    
    if current_env_url and check_url_status(current_env_url):
        result['message'] = 'URL actual está funcionando correctamente'
        print(json.dumps(result))
        return
    
    # La URL no funciona o es diferente, actualizar
    if current_ngrok_url != current_env_url:
        if update_env_file(current_ngrok_url):
            if restart_n8n():
                result['url_changed'] = True
                result['message'] = f'URL actualizada de {current_env_url} a {current_ngrok_url}'
            else:
                result['status'] = 'error'
                result['message'] = 'URL actualizada pero falló el reinicio de n8n'
        else:
            result['status'] = 'error'
            result['message'] = 'Error actualizando el archivo .env'
    else:
        result['message'] = 'URL de ngrok no ha cambiado pero no responde'
    
    print(json.dumps(result))

if __name__ == '__main__':
    main()