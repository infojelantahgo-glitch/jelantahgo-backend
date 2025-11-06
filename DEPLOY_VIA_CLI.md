# 🚀 Deploy via CLI - Railway

Panduan deploy aplikasi ke Railway menggunakan CLI.

---

## 📋 Prerequisites

1. **Railway account** sudah dibuat
2. **Railway CLI** terinstall
3. **Project sudah di GitHub**

---

## 🔧 Step 1: Install Railway CLI

### Windows (via npm):

```bash
npm install -g @railway/cli
```

### Verify Installation:

```bash
railway --version
```

---

## 🔐 Step 2: Login ke Railway

```bash
railway login
```

Ini akan membuka browser untuk login dengan GitHub.

---

## 📁 Step 3: Initialize Railway Project

```bash
railway init
```

Pilih:
- **Link to existing project?** → No (buat baru)
- **Project name:** `jelantahgo-backend`

---

## 🔗 Step 4: Link ke GitHub Repository (Opsional)

Jika ingin auto-deploy dari GitHub:

1. **Via Railway Dashboard:**
   - Buka dashboard
   - Project → Settings → Source
   - Connect GitHub repository

2. **Atau deploy langsung via CLI** (tidak perlu link GitHub)

---

## 📤 Step 5: Deploy

### Deploy dari Local:

```bash
railway up
```

Ini akan:
- Build aplikasi
- Deploy ke Railway
- Show deployment URL

---

## 🔧 Step 6: Setup Environment Variables

### Via CLI:

```bash
# Set DATABASE_URL
railway variables set DATABASE_URL="postgresql://postgres:jelantahgo-db@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres"

# Set JWT_SECRET (generate dulu)
railway variables set JWT_SECRET="$(python -c 'import secrets; print(secrets.token_urlsafe(32))')"

# Set API_HOST
railway variables set API_HOST="0.0.0.0"

# Set API_PORT
railway variables set API_PORT="8000"
```

### Via Dashboard (Lebih Mudah):

1. Buka Railway Dashboard
2. Project → Variables
3. Add variables manual

---

## ✅ Step 7: Verify Deployment

```bash
# Cek logs
railway logs

# Cek status
railway status

# Open in browser
railway open
```

---

## 🔍 Alternative: Render CLI

Jika ingin pakai Render CLI:

### Install Render CLI:

```bash
npm install -g render-cli
```

### Login:

```bash
render login
```

### Deploy:

```bash
render deploy
```

---

## 📚 Railway CLI Commands

```bash
# Login
railway login

# Initialize project
railway init

# Deploy
railway up

# View logs
railway logs

# Open dashboard
railway open

# Set variables
railway variables set KEY=value

# List variables
railway variables

# Connect to database
railway connect

# Run command
railway run <command>
```

---

## 🎯 Quick Deploy Script

Buat file `deploy.sh` atau `deploy.bat`:

### Windows (deploy.bat):

```batch
@echo off
echo Deploying to Railway...
railway login
railway init
railway variables set DATABASE_URL="postgresql://postgres:jelantahgo-db@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres"
railway variables set JWT_SECRET="your-secret-here"
railway variables set API_HOST="0.0.0.0"
railway variables set API_PORT="8000"
railway up
echo Deployment complete!
```

### Linux/Mac (deploy.sh):

```bash
#!/bin/bash
echo "Deploying to Railway..."
railway login
railway init
railway variables set DATABASE_URL="postgresql://postgres:jelantahgo-db@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres"
railway variables set JWT_SECRET="$(python3 -c 'import secrets; print(secrets.token_urlsafe(32))')"
railway variables set API_HOST="0.0.0.0"
railway variables set API_PORT="8000"
railway up
echo "Deployment complete!"
```

---

## 🆘 Troubleshooting

### Error: "not logged in"

**Solusi:**
```bash
railway login
```

### Error: "project not found"

**Solusi:**
```bash
railway init
```

### Error: "deployment failed"

**Solusi:**
```bash
railway logs
# Cek error message
```

---

## ✅ Checklist

- [ ] Install Railway CLI
- [ ] Login: `railway login`
- [ ] Initialize: `railway init`
- [ ] Set environment variables
- [ ] Deploy: `railway up`
- [ ] Verify: Test `/health` endpoint

---

**Selamat deploy! 🚀**

