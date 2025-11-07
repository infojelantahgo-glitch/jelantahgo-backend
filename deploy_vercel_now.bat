@echo off
echo ========================================
echo   DEPLOY BACKEND KE VERCEL
echo ========================================
echo.

REM Check if logged in
vercel whoami >nul 2>&1
if errorlevel 1 (
    echo [INFO] Please login to Vercel first...
    vercel login
    if errorlevel 1 (
        echo [ERROR] Login failed
        pause
        exit /b 1
    )
)

echo [OK] Logged in to Vercel!
echo.

REM Set environment variables (optional, bisa set manual di dashboard)
echo [INFO] Setting environment variables...
echo.
echo Please set these manually in Vercel Dashboard:
echo   DATABASE_URL=postgresql://postgres.ybzzfgzzfrozxrujmjeo:jelantahgo-db@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres
echo   JWT_SECRET=FoJr8-mQNKJ-CX3R_xj5dKO1JGXbbEattsutJiIaA-s
echo.

REM Deploy
echo [INFO] Deploying to Vercel...
echo.
vercel --prod

if errorlevel 1 (
    echo [ERROR] Deployment failed
    pause
    exit /b 1
)

echo.
echo [SUCCESS] Deployment completed!
echo.
pause

