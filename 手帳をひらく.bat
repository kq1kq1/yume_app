@echo off
chcp 65001 >nul
title Yume Techo
cd /d "%~dp0"

python "_launcher.py"
if not errorlevel 1 goto :eof

py "_launcher.py"
if not errorlevel 1 goto :eof

echo.
echo Python が見つかりませんでした。
echo 「index.html」を直接ダブルクリックして開いてください。
echo.
pause
