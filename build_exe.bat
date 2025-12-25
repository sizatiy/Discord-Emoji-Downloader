@echo off
echo Building Discord Emoji Downloader EXE...
echo.

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
) else (
    call venv\Scripts\activate.bat
)

echo Installing dependencies...
pip install -q -r requirements.txt
pip install -q pyinstaller

echo Building EXE...
pyinstaller --onefile --name "Discord Emoji Downloader" --icon=emoji.ico emoji_downloader.py 2>nul

if exist dist\emoji_downloader.exe (
    echo.
    echo ✓ Build complete!
    echo ✓ EXE file: dist\emoji_downloader.exe
    echo.
    echo You can now:
    echo 1. Share the EXE file with others
    echo 2. Move it anywhere you want
    echo 3. Double-click it to run
) else (
    echo.
    echo ❌ Build failed. Make sure PyInstaller is installed.
)

pause
