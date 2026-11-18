@echo off
echo.
echo ========================================
echo    Iniciando n8n + PostgreSQL + Sandbox
echo ========================================
echo.

docker-compose up -d --build

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ Contenedores iniciados correctamente
    echo.
    echo 📱 Accesos:
    echo    - n8n local:      http://localhost:5678
    echo    - Sandbox API:    http://localhost:3200
    echo.
    echo ℹ️ ngrok esta detenido por defecto. Para iniciarlo cuando configures ngrok.yml:
    echo    docker-compose --profile ngrok up -d ngrok
    echo.
) else (
    echo.
    echo ❌ Error al iniciar los contenedores
    echo.
)

pause