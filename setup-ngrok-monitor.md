# 🔄 Monitor automático de URL ngrok

## ¿Qué hace?

Este flujo de n8n se ejecuta **todos los días a las 12:00 AM** y:

1. ✅ Verifica si la URL actual de ngrok está funcionando
2. 🔄 Si no funciona, obtiene la nueva URL de ngrok
3. 📝 Actualiza automáticamente el archivo `.env`
4. 🔄 Reinicia el contenedor de n8n
5. 📱 Te envía una notificación por Telegram

## 📋 Configuración

### 1. Variables de entorno (opcional para notificaciones)

Agrega a tu `.env`:
```bash
# Para notificaciones Telegram (opcional)
TELEGRAM_BOT_TOKEN=tu_bot_token_aqui
TELEGRAM_CHAT_ID=tu_chat_id_aqui
```

### 2. Importar el flujo en n8n

1. Abre n8n en http://localhost:5678
2. Ve a **Workflows** → **Import from file**
3. Selecciona el archivo `n8n-workflow-ngrok-monitor.json`
4. Activa el workflow

### 3. Configurar notificaciones Telegram (opcional)

Si quieres recibir notificaciones:

1. **Crear bot de Telegram:**
   - Habla con @BotFather en Telegram
   - Usa `/newbot` y sigue las instrucciones
   - Guarda el token que te da

2. **Obtener tu Chat ID:**
   - Envía un mensaje a tu bot
   - Ve a: `https://api.telegram.org/bot<TU_TOKEN>/getUpdates`
   - Busca tu `chat_id` en la respuesta

3. **Configurar variables en n8n:**
   - Ve a **Settings** → **Variables**
   - Agrega:
     - `TELEGRAM_BOT_TOKEN`: tu token del bot
     - `TELEGRAM_CHAT_ID`: tu chat ID

## 🔧 Cómo funciona

### Flujo del workflow:

```
12:00 AM diario
    ↓
Obtener URL de ngrok (localhost:4040/api/tunnels)
    ↓
Verificar si URL actual funciona (/healthz)
    ↓
¿Funciona? → SÍ → Log "Todo OK"
    ↓
   NO
    ↓
Actualizar .env con nueva URL
    ↓
Reiniciar contenedor n8n
    ↓
Enviar notificación
```

### Comandos que ejecuta:

```bash
# Actualizar .env
docker exec n8n-app sh -c 'sed -i "s|N8N_WEBHOOK_URL=.*|N8N_WEBHOOK_URL=nueva_url|" /opt/n8n/.env'

# Reiniciar n8n
docker restart n8n-app
```

## 📱 Notificaciones

Recibirás mensajes como:

**✅ Cuando todo está OK:**
```
✅ URL de n8n funcionando correctamente

📅 Fecha: 01/01/2024 00:00:00
🔗 URL actual: https://abc123.ngrok-free.dev
✅ Estado: Funcionando correctamente

No se requiere ninguna acción.
```

**🔄 Cuando se actualiza:**
```
🔄 URL de n8n actualizada

📅 Fecha: 01/01/2024 00:00:00
🔗 URL anterior: https://old123.ngrok-free.dev
🆕 URL nueva: https://new456.ngrok-free.dev

✅ El servicio ha sido reiniciado correctamente.
```

## 🛠️ Personalización

### Cambiar horario de verificación:

En el nodo "Cron - Diario 12AM", modifica la expresión cron:
- `0 0 * * *` = 12:00 AM diario
- `0 12 * * *` = 12:00 PM diario  
- `0 */6 * * *` = Cada 6 horas

### Verificación manual:

Puedes ejecutar el workflow manualmente desde n8n para probar.

## 🔒 Seguridad

- El workflow tiene acceso al Docker socket para reiniciarse
- Solo modifica la variable `N8N_WEBHOOK_URL` en `.env`
- Las notificaciones son opcionales

## 🐛 Troubleshooting

### El workflow no se ejecuta:
- Verifica que esté **activado** en n8n
- Revisa los logs en **Executions**

### No recibo notificaciones:
- Verifica las variables `TELEGRAM_BOT_TOKEN` y `TELEGRAM_CHAT_ID`
- Prueba enviando un mensaje manual al bot

### Error al reiniciar:
- Verifica que el volumen Docker socket esté montado
- Revisa permisos del usuario en el contenedor