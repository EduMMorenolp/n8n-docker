@echo off
echo.
echo ========================================
echo    Deteniendo n8n + PostgreSQL + ngrok
echo ========================================
echo.

docker-compose down

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✅ Contenedores detenidos correctamente
    echo.
) else (
    echo.
    echo ❌ Error al detener los contenedores
    echo.
)

pause