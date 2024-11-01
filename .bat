@echo off
chcp 65001 >nul
CALL "venv/Scripts/activate.bat"
start "Judge Server" python "main.py"
exit|