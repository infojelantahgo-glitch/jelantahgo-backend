#!/bin/bash

echo "========================================"
echo "  VERCEL CLI SETUP & DEPLOY"
echo "========================================"
echo ""

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "[INFO] Installing Vercel CLI..."
    npm install -g vercel
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to install Vercel CLI"
        exit 1
    fi
fi

echo "[OK] Vercel CLI is installed!"
echo ""

# Check if user is logged in
vercel whoami &> /dev/null
if [ $? -ne 0 ]; then
    echo "[INFO] Please login to Vercel..."
    echo "[INFO] This will open a browser for authentication"
    vercel login
    if [ $? -ne 0 ]; then
        echo "[ERROR] Login failed"
        exit 1
    fi
else
    echo "[OK] Already logged in to Vercel!"
    vercel whoami
fi

echo ""
echo "========================================"
echo "  READY TO DEPLOY!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Navigate to your frontend directory"
echo "2. Run: vercel"
echo "3. Or run: vercel --prod (for production)"
echo ""
echo "Example:"
echo "  cd jelantahgo-frontend"
echo "  vercel --prod"
echo ""

