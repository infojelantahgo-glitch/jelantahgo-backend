@echo off
echo ========================================
echo   VERCEL CLI SETUP & DEPLOY
echo ========================================
echo.

REM Check if Vercel CLI is installed
vercel --version >nul 2>&1
if errorlevel 1 (
    echo [INFO] Installing Vercel CLI...
    npm install -g vercel
    if errorlevel 1 (
        echo [ERROR] Failed to install Vercel CLI
        pause
        exit /b 1
    )
)

echo [OK] Vercel CLI is installed!
echo.

REM Check if user is logged in
vercel whoami >nul 2>&1
if errorlevel 1 (
    echo [INFO] Please login to Vercel...
    echo [INFO] This will open a browser for authentication
    vercel login
    if errorlevel 1 (
        echo [ERROR] Login failed
        pause
        exit /b 1
    )
) else (
    echo [OK] Already logged in to Vercel!
    vercel whoami
)

echo.
echo ========================================
echo   READY TO DEPLOY!
echo ========================================
echo.
echo Next steps:
echo 1. Navigate to your frontend directory
echo 2. Run: vercel
echo 3. Or run: vercel --prod (for production)
echo.
echo Example:
echo   cd jelantahgo-frontend
echo   vercel --prod
echo.
pause

