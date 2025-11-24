# n8n con PostgreSQL y ngrok

Stack completo de n8n con base de datos PostgreSQL y túnel público ngrok para webhooks.

## 🚀 Inicio rápido

### Opción 1: Scripts de Windows
```cmd
# Iniciar todo
start.bat

# Detener todo
stop.bat
```

### Opción 2: Docker Compose
```bash
# Iniciar contenedores
docker-compose up -d

# Detener contenedores
docker-compose down

# Ver logs
docker-compose logs -f n8n
```

## ⚙️ Configuración inicial

### 1. Variables de entorno
```bash
# Copia el archivo de ejemplo
cp .env.example .env

# Edita las variables necesarias
# - POSTGRES_PASSWORD: Cambia la contraseña por defecto
# - NGROK_AUTHTOKEN: Tu token de ngrok
# - N8N_WEBHOOK_URL: URL pública de ngrok (actualizar después)
```

### 2. Configurar ngrok
```bash
# Copia el archivo de ejemplo
cp ngrok_example.yml ngrok.yml

# Edita ngrok.yml con tu authtoken real
```

1. Regístrate en https://ngrok.com
2. Obtén tu authtoken desde el dashboard
3. Reemplaza `YOUR_NGROK_AUTH_TOKEN` en `ngrok.yml`
4. Inicia los contenedores

## 🌐 Accesos

| Servicio | URL Local | Puerto |
|----------|-----------|--------|
| n8n | http://localhost:5678 | 5678 |
| PostgreSQL | localhost:5433 | 5433 |
| ngrok Dashboard | http://localhost:4040 | 4040 |

## 📋 Estructura del proyecto

```
n8n docker/
├── .env.example          # Variables de entorno de ejemplo
├── .env                  # Variables de entorno (crear desde .example)
├── .gitignore           # Archivos ignorados por git
├── docker-compose.yml   # Configuración de contenedores
├── ngrok_example.yml    # Configuración de ngrok de ejemplo
├── ngrok.yml           # Configuración de ngrok (crear desde example)
├── start.bat           # Script de inicio para Windows
├── stop.bat            # Script de parada para Windows
└── README.md           # Esta documentación
```

## 🔧 Configuración avanzada

### Variables de entorno disponibles

```bash
# Base de datos
POSTGRES_DB=n8n
POSTGRES_USER=n8n
POSTGRES_PASSWORD=change_this_password

# n8n
N8N_TIMEZONE=America/Argentina/Buenos_Aires

# ngrok
NGROK_AUTHTOKEN=your_ngrok_auth_token_here
N8N_WEBHOOK_URL=https://your-ngrok-url.ngrok-free.dev
```

### Actualizar URL de webhook

1. Obtén la URL pública desde http://localhost:4040
2. Actualiza `N8N_WEBHOOK_URL` en `.env`
3. Reinicia n8n: `docker-compose restart n8n`

### Comandos útiles

```bash
# Ver logs específicos
docker-compose logs -f postgres
docker-compose logs -f ngrok

# Reiniciar servicios individuales
docker-compose restart n8n
docker-compose restart postgres
docker-compose restart ngrok

# Acceder al contenedor de PostgreSQL
docker-compose exec postgres psql -U n8n -d n8n

# Backup de la base de datos
docker-compose exec postgres pg_dump -U n8n n8n > backup.sql

# Restaurar backup
docker-compose exec -T postgres psql -U n8n -d n8n < backup.sql
```

## 🔒 Seguridad

- ✅ Las credenciales están en variables de entorno
- ✅ Los archivos sensibles están en `.gitignore`
- ⚠️ Cambia `POSTGRES_PASSWORD` antes de usar en producción
- ⚠️ ngrok expone tu instancia públicamente

## 🐛 Solución de problemas

### n8n no inicia
```bash
# Verificar que PostgreSQL esté listo
docker-compose logs postgres

# Verificar healthcheck
docker-compose ps
```

### ngrok no conecta
```bash
# Verificar authtoken en ngrok.yml
docker-compose logs ngrok

# Verificar dashboard
curl http://localhost:4040/api/tunnels
```

### Webhooks no funcionan
1. Verifica que la URL en `.env` coincida con ngrok
2. Reinicia n8n después de cambiar la URL
3. Usa HTTPS, no HTTP para webhooks

## 📚 Recursos

- [Documentación de n8n](https://docs.n8n.io/)
- [ngrok Documentation](https://ngrok.com/docs)
- [PostgreSQL Docker](https://hub.docker.com/_/postgres)