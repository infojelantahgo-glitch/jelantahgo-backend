# ✅ Deployment Checklist - JelantahGO Backend

## 📋 Checklist Lengkap untuk Deploy

---

## ✅ 1. Database Setup (Sudah Selesai)

- [x] Supabase project dibuat: `jelantahgo-db`
- [x] Connection string tersedia
- [x] Migration files sudah dibuat
- [x] Tabel sudah dibuat/rename (jika diperlukan)

**Connection String:**
```
postgresql://postgres:jelantahgo-db@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres
```

---

## ✅ 2. Code Repository (Sudah Selesai)

- [x] Code sudah di GitHub: `infojelantahgo-glitch/jelantahgo-backend`
- [x] Semua file sudah di-commit
- [x] Migration files sudah ada
- [x] Config files sudah ada

**Repository:** https://github.com/infojelantahgo-glitch/jelantahgo-backend

---

## 📋 3. Deploy Backend (Pilih Salah Satu)

### Opsi A: Railway (Recommended) ⭐

- [ ] Sign up di [railway.app](https://railway.app)
- [ ] New Project → Deploy from GitHub
- [ ] Pilih: `infojelantahgo-glitch/jelantahgo-backend`
- [ ] Set environment variables:
  - [ ] `DATABASE_URL` = (connection string Supabase)
  - [ ] `JWT_SECRET` = (generate random string)
  - [ ] `API_HOST` = `0.0.0.0`
  - [ ] `API_PORT` = `8000`
- [ ] Deploy
- [ ] Verify: Test `/health` endpoint

### Opsi B: Render

- [ ] Sign up di [render.com](https://render.com)
- [ ] New → Web Service → Connect GitHub
- [ ] Pilih: `infojelantahgo-glitch/jelantahgo-backend`
- [ ] Set environment variables:
  - [ ] `DATABASE_URL` = (connection string Supabase)
  - [ ] `JWT_SECRET` = (generate random string)
  - [ ] `API_HOST` = `0.0.0.0`
  - [ ] `API_PORT` = `10000`
- [ ] Deploy
- [ ] Verify: Test `/health` endpoint

---

## ✅ 4. Environment Variables

### Required Variables:

```env
DATABASE_URL=postgresql://postgres:jelantahgo-db@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres
JWT_SECRET=<generate-random-string>
API_HOST=0.0.0.0
API_PORT=8000  # atau 10000 untuk Render
```

### Generate JWT_SECRET:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### Optional Variables (untuk email):

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
EMAIL_FROM=your-email@gmail.com
```

---

## ✅ 5. Verify Deployment

### Test Health Check:

```
https://your-app-url/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "service": "JelantahGO Backend"
}
```

### Test API Documentation:

- **Swagger UI:** `https://your-app-url/docs`
- **ReDoc:** `https://your-app-url/redoc`

### Test Database Connection:

1. Buka `/docs`
2. POST `/auth/register`
3. Isi data user
4. Execute
5. Jika berhasil → Database connection OK! ✅

---

## ✅ 6. Verify Database Tables

Di Supabase Dashboard → Table Editor, pastikan ada:

- [ ] `users`
- [ ] `customers`
- [ ] `orders`
- [ ] `billings`
- [ ] `chat_messages`
- [ ] `courier_locations`
- [ ] `payment_proofs`

---

## 🎯 Quick Start Commands

### Generate JWT_SECRET:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### Test Health Check:
```bash
curl https://your-app-url/health
```

### Test Register User:
```bash
curl -X POST "https://your-app-url/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "test123",
    "role": "customer",
    "name": "Test User"
  }'
```

---

## 📚 Documentation Files

- **DEPLOY_INSTRUCTIONS.md** - Panduan deploy ke Render
- **SUPABASE_ENV_SETUP.md** - Setup environment variables
- **QUICK_START_SUPABASE.md** - Quick start Supabase
- **FIX_TABLE_NAMES.md** - Fix masalah nama tabel
- **ALTERNATIVE_DEPLOY.md** - Platform alternatif

---

## ✅ Final Checklist

- [ ] Database connection string sudah ada
- [ ] Tabel sudah dibuat (Indonesia → Inggris atau baru)
- [ ] Aplikasi sudah di-deploy ke Railway/Render
- [ ] Environment variables sudah di-set
- [ ] Health check endpoint berhasil
- [ ] API docs bisa diakses
- [ ] Test register user berhasil
- [ ] Database tables terverifikasi

---

## 🎉 Selesai!

Setelah semua checklist selesai, aplikasi siap digunakan!

**API Base URL:**
- Railway: `https://your-app.up.railway.app`
- Render: `https://your-app.onrender.com`

**API Documentation:**
- `/docs` - Swagger UI
- `/redoc` - ReDoc

---

**Selamat! Aplikasi sudah online! 🚀**

