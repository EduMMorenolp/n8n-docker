@echo off
echo.
echo ========================================
echo    Iniciando n8n + PostgreSQL + ngrok
echo ========================================
echo.

docker-compose up -d --build

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ Contenedores iniciados correctamente
    echo.
    echo 📱 Accesos:
    echo    - n8n local:      http://localhost:5678
    echo    - ngrok dashboard: http://localhost:4040
    echo.
    echo 🔗 Para obtener la URL publica:
    echo    Visita http://localhost:4040 y copia la URL HTTPS
    echo.
) else (
    echo.
    echo ❌ Error al iniciar los contenedores
    echo.
)

pause