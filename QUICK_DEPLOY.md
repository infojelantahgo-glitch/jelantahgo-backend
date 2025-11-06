# ⚡ Quick Deploy via Railway CLI

Panduan cepat deploy aplikasi ke Railway menggunakan CLI.

---

## 🚀 Langkah Cepat

### 1. Login ke Railway (Manual - Butuh Browser)

Buka terminal dan jalankan:

```bash
railway login
```

Ini akan membuka browser untuk login dengan GitHub. Setelah login berhasil, lanjutkan ke step 2.

---

### 2. Jalankan Script Deploy

**Windows:**
```bash
.\deploy_railway.bat
```

**Linux/Mac:**
```bash
chmod +x deploy_railway.sh
./deploy_railway.sh
```

---

### 3. Atau Deploy Manual

Jika script tidak berjalan, jalankan command manual:

```bash
# Initialize project
railway init

# Set environment variables
railway variables set DATABASE_URL="postgresql://postgres:jelantahgo-db@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres"

railway variables set JWT_SECRET="$(python -c 'import secrets; print(secrets.token_urlsafe(32))')"

railway variables set API_HOST="0.0.0.0"

railway variables set API_PORT="8000"

# Deploy
railway up
```

---

## ✅ Verify Deployment

Setelah deploy selesai:

```bash
# Cek logs
railway logs

# Buka dashboard
railway open

# Cek status
railway status
```

---

## 🔗 Test Aplikasi

Setelah deploy, test aplikasi:

```bash
# Health check
curl https://your-app.up.railway.app/health

# Atau buka di browser
# https://your-app.up.railway.app/docs
```

---

## 📋 Checklist

- [ ] Railway CLI terinstall: `railway --version`
- [ ] Login: `railway login` (manual, buka browser)
- [ ] Initialize: `railway init`
- [ ] Set environment variables
- [ ] Deploy: `railway up`
- [ ] Verify: Test `/health` endpoint

---

## 🆘 Troubleshooting

### Error: "not logged in"
**Solusi:** Jalankan `railway login` lagi

### Error: "project not found"
**Solusi:** Jalankan `railway init` untuk membuat project baru

### Error: "deployment failed"
**Solusi:** 
```bash
railway logs
# Cek error message dan fix
```

---

**Selamat deploy! 🚀**

