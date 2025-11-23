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