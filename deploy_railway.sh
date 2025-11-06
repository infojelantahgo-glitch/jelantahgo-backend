#!/bin/bash
# ====================================
# Deploy JelantahGO Backend ke Railway
# ====================================

echo "========================================"
echo "  DEPLOY KE RAILWAY"
echo "========================================"
echo ""

# Step 1: Login (akan buka browser)
echo "[1/5] Login ke Railway..."
echo "Buka browser yang muncul dan login dengan GitHub"
railway login || {
    echo "ERROR: Login gagal!"
    exit 1
}

# Step 2: Initialize project (jika belum)
echo ""
echo "[2/5] Initialize Railway project..."
railway init || echo "WARNING: Init mungkin sudah ada, lanjutkan..."

# Step 3: Set environment variables
echo ""
echo "[3/5] Setup environment variables..."
railway variables set DATABASE_URL="postgresql://postgres:jelantahgo-db@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres"
railway variables set API_HOST="0.0.0.0"
railway variables set API_PORT="8000"

# Step 4: Generate and set JWT_SECRET
echo ""
echo "[4/5] Generate JWT_SECRET..."
JWT_SECRET=$(python3 -c "import secrets; print(secrets.token_urlsafe(32))")
railway variables set JWT_SECRET="$JWT_SECRET"

# Step 5: Deploy
echo ""
echo "[5/5] Deploying to Railway..."
railway up || {
    echo "ERROR: Deployment gagal!"
    exit 1
}

echo ""
echo "========================================"
echo "  DEPLOYMENT SELESAI!"
echo "========================================"
echo ""
echo "Cek status di: railway open"
echo ""

