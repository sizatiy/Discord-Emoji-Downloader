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
pip install -r requirements.txt
pip install pyinstaller

echo Building EXE...
pyinstaller --onefile --windowed --name "Discord Emoji Downloader" emoji_downloader_gui.py

if exist "dist\Discord Emoji Downloader.exe" (
    echo.
    echo ✓ Build complete!
    echo ✓ EXE file: dist\Discord Emoji Downloader.exe
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
