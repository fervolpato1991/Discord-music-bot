@echo off
cd /d %~dp0\service

CamaleonDJBot.exe stop
CamaleonDJBot.exe uninstall

echo Servicio eliminado
pause