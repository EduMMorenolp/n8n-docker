# n8n con PostgreSQL

## Iniciar los contenedores
```bash
docker-compose up -d
```

## Detener los contenedores
```bash
docker-compose down
```

## Ver logs
```bash
docker-compose logs -f n8n
```

## Acceder a n8n
http://localhost:5678

## Configuración
- Edita el archivo `.env` para cambiar credenciales
- PostgreSQL corre en el puerto interno 5432
- n8n está disponible en el puerto 5678
- ngrok dashboard: http://localhost:4040

## Configurar ngrok
1. Regístrate en https://ngrok.com
2. Obtén tu authtoken
3. Reemplaza `YOUR_NGROK_AUTH_TOKEN` en `ngrok.yml`
4. Reinicia los contenedores

## URLs públicas
- Local: http://localhost:5678
- Pública: Ver en http://localhost:4040 (ngrok dashboard)

## Configurar URL de Webhook
1. Copia la URL HTTPS de ngrok dashboard
2. Actualiza `WEBHOOK_URL` en docker-compose.yml
3. Reinicia: `docker-compose restart n8n`

## Solución rápida para webhooks
Si cambias la URL de ngrok, actualiza estas variables:
- `WEBHOOK_URL` en docker-compose.yml
- `N8N_EDITOR_BASE_URL` en docker-compose.yml