@echo off
chcp 65001 >nul
CALL "venv/Scripts/activate.bat"

:menu
echo ========================================
echo 請選擇要啟動的選項：
echo 1. 啟動 Judge Server
echo 2. 啟動 Discord Bot
echo 3. 同時啟動 Judge Server 和 Discord Bot
echo 4. 退出
echo ========================================
set /p choice="請輸入您的選擇 (1-4): "

if "%choice%"=="1" (
    start "Judge Server" python "main.py"
    goto end
) else if "%choice%"=="2" (
    start "Discord Bot" python "bot.py"
    goto end
) else if "%choice%"=="3" (
    start "Judge Server" python "judge.py"
    start "Discord Bot" python "bot.py"
    goto end
) else if "%choice%"=="4" (
    goto end
) else (
    echo 選擇無效，請輸入有效的選項。
    goto menu
)
:end
exit|