@echo off
cd /d %~dp0

echo Verificando servicio...

sc query CamaleonDJBot >nul 2>&1
if %errorlevel%==0 (
    echo Servicio ya instalado.
    echo Reiniciando servicio...

    cd service
    CamaleonDJBot.exe restart

    echo Listo.
    pause
    exit
)

echo ================================
echo Instalando CamaleonDJ Bot
echo ================================

if not exist venv (
    echo Creando entorno virtual...
    python -m venv venv
)

call venv\Scripts\activate

echo Instalando dependencias...
pip install -r requirements.txt

if not exist logs mkdir logs

cd service

CamaleonDJBot.exe install
CamaleonDJBot.exe start

echo ================================
echo BOT INSTALADO Y CORRIENDO
echo ================================
pause