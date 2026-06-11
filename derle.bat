@echo off
echo ============================================
echo   PyBall - Derleme Araci
echo ============================================
echo.

:: PyInstaller kurulu mu?
pyinstaller --version >nul 2>&1
if errorlevel 1 (
    echo PyInstaller bulunamadi. Kuruluyor...
    pip install pyinstaller
    if errorlevel 1 (
        echo HATA: PyInstaller kurulanamadi!
        pause
        exit /b 1
    )
)

:: Eski derleme kalıntilarini temizle
if exist "build"       rmdir /s /q build
if exist "dist"        rmdir /s /q dist
if exist "pyBall.spec" del /q pyBall.spec

echo Derleniyor...
echo.

:: UPX var mi? (kucuk boyut icin)
set UPX_FLAG=
if exist "upx.exe"        set UPX_FLAG=--upx-dir .
if exist "C:\upx\upx.exe" set UPX_FLAG=--upx-dir C:\upx

pyinstaller ^
    --onefile ^
    --noconsole ^
    --name pyBall ^
    --icon=pyBall.ico ^
    %UPX_FLAG% ^
    pyBall.py

if errorlevel 1 (
    echo.
    echo HATA: Derleme basarisiz!
    pause
    exit /b 1
)

:: Build klasorunu ve spec dosyasini temizle
if exist "build"       rmdir /s /q build
if exist "pyBall.spec" del /q pyBall.spec

echo.
echo ============================================
echo   Tamamlandi!  -^>  dist\pyBall.exe
echo ============================================
echo.
pause
