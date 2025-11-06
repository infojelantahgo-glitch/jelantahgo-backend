# 🟣 Setup Supabase untuk Database

Supabase adalah alternatif Firebase dengan PostgreSQL database gratis. Kita akan gunakan Supabase untuk database, dan deploy backend ke Railway/Render.

---

## 📋 Overview

- **Database:** Supabase (PostgreSQL 500MB gratis)
- **Backend:** Railway atau Render (untuk deploy FastAPI)
- **Connection:** Backend connect ke Supabase database

---

## 🚀 Step 1: Setup Supabase Database

### 1.1 Buat Akun Supabase

1. **Buka [supabase.com](https://supabase.com)**
2. **Klik "Start your project"**
3. **Sign up dengan GitHub** (paling mudah)
4. **Verifikasi email** (jika diminta)

### 1.2 Buat Project Baru

1. **Klik "New Project"**
2. **Isi form:**
   - **Organization:** Pilih atau buat baru
   - **Name:** `jelantahgo-backend`
   - **Database Password:** Buat password yang kuat (simpan baik-baik!)
   - **Region:** Pilih yang terdekat (Singapore/US)
   - **Pricing Plan:** Free
3. **Klik "Create new project"**
4. **Tunggu setup selesai** (~2 menit)

### 1.3 Dapatkan Connection String

1. **Di project dashboard, klik "Settings" (ikon gear)**
2. **Pilih "Database"** di sidebar kiri
3. **Scroll ke "Connection string"**
4. **Pilih tab "URI"**
5. **Copy connection string** yang formatnya seperti:
   ```
   postgresql://postgres:[YOUR-PASSWORD]@db.xxxxx.supabase.co:5432/postgres
   ```
   **PENTING:** Ganti `[YOUR-PASSWORD]` dengan password yang Anda buat!

6. **Atau gunakan "Connection pooling"** (recommended untuk production):
   - Tab "Connection pooling"
   - Copy connection string (format: `postgresql://postgres.xxxxx:xxxxx@aws-0-xx-xxx.pooler.supabase.com:6543/postgres`)

### 1.4 Update Connection String

**Format yang benar:**
```
postgresql://postgres:YOUR_PASSWORD@db.xxxxx.supabase.co:5432/postgres
```

**Ganti:**
- `YOUR_PASSWORD` = password yang Anda buat saat setup project

---

## 🚂 Step 2: Deploy Backend ke Railway (Recommended)

### 2.1 Sign Up Railway

1. **Buka [railway.app](https://railway.app)**
2. **Sign up dengan GitHub**

### 2.2 Deploy Backend

1. **Klik "New Project"**
2. **Pilih "Deploy from GitHub repo"**
3. **Pilih repository:** `infojelantahgo-glitch/jelantahgo-backend`
4. **Railway akan otomatis detect dan deploy**

### 2.3 Setup Environment Variables

1. **Di Railway project, klik service yang baru dibuat**
2. **Klik tab "Variables"**
3. **Tambahkan environment variables:**

   **Variable 1: DATABASE_URL**
   ```
   Key: DATABASE_URL
   Value: postgresql://postgres:YOUR_PASSWORD@db.xxxxx.supabase.co:5432/postgres
   ```
   (Ganti dengan connection string dari Supabase)

   **Variable 2: JWT_SECRET**
   ```
   Key: JWT_SECRET
   Value: [generate random string]
   ```
   Generate dengan:
   ```bash
   python -c "import secrets; print(secrets.token_urlsafe(32))"
   ```

   **Variable 3: API_HOST**
   ```
   Key: API_HOST
   Value: 0.0.0.0
   ```

   **Variable 4: API_PORT**
   ```
   Key: API_PORT
   Value: 8000
   ```

   **Variable 5-9 (Opsional - untuk email):**
   ```
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=587
   SMTP_USER=your-email@gmail.com
   SMTP_PASSWORD=your-app-password
   EMAIL_FROM=your-email@gmail.com
   ```

### 2.4 Deploy

- Railway akan otomatis redeploy setelah environment variables diubah
- Atau klik "Deploy" manual

---

## 🎨 Alternatif: Deploy ke Render

Jika tidak bisa pakai Railway, gunakan Render:

### 2.1 Setup Render Web Service

1. **Buka [render.com](https://render.com)**
2. **New → Web Service**
3. **Connect GitHub repository:** `infojelantahgo-glitch/jelantahgo-backend`
4. **Settings:**
   - Name: `jelantahgo-backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`
   - Plan: `Free`

### 2.2 Setup Environment Variables

1. **Tab "Environment"**
2. **Add Environment Variables:**

   **Variable 1: DATABASE_URL**
   ```
   Key: DATABASE_URL
   Value: postgresql://postgres:YOUR_PASSWORD@db.xxxxx.supabase.co:5432/postgres
   ```
   (Ganti dengan connection string dari Supabase)

   **Variable 2: JWT_SECRET**
   ```
   Key: JWT_SECRET
   Value: [generate random string]
   ```

   **Variable 3: API_HOST**
   ```
   Key: API_HOST
   Value: 0.0.0.0
   ```

   **Variable 4: API_PORT**
   ```
   Key: API_PORT
   Value: 10000
   ```
   (Render menggunakan port 10000, bukan 8000)

### 2.3 Deploy

- Render akan otomatis deploy
- Tunggu sampai status "Live"

---

## ✅ Step 3: Verifikasi Setup

### 3.1 Test Database Connection

1. **Buka URL aplikasi:**
   - Railway: `https://your-app.up.railway.app`
   - Render: `https://your-app.onrender.com`

2. **Test health check:**
   ```
   https://your-app-url/health
   ```
   Seharusnya return:
   ```json
   {
     "status": "healthy",
     "service": "JelantahGO Backend"
   }
   ```

### 3.2 Test Database

1. **Buka API docs:**
   ```
   https://your-app-url/docs
   ```

2. **Test register user:**
   - POST `/auth/register`
   - Isi data user
   - Klik "Execute"
   - Jika berhasil, berarti database connection OK!

### 3.3 Cek Supabase Dashboard

1. **Buka Supabase dashboard**
2. **Table Editor**
3. **Cek apakah tabel sudah dibuat:**
   - `users`
   - `customers`
   - `orders`
   - `billings`
   - dll

---

## 🔧 Troubleshooting

### Database Connection Error

**Error:** `could not connect to server`

**Solusi:**
1. **Cek connection string format:**
   - Pastikan password benar
   - Pastikan host/port benar
   - Format: `postgresql://postgres:PASSWORD@HOST:5432/postgres`

2. **Cek Supabase Settings:**
   - Settings → Database → Connection string
   - Pastikan menggunakan password yang benar

3. **Cek Network Access:**
   - Settings → Database → Connection pooling
   - Pastikan IP tidak di-block

### Password Error

**Error:** `password authentication failed`

**Solusi:**
1. **Reset password di Supabase:**
   - Settings → Database → Database password
   - Reset password
   - Update `DATABASE_URL` di Railway/Render

### Connection Timeout

**Error:** `connection timeout`

**Solusi:**
1. **Gunakan Connection Pooling:**
   - Di Supabase, gunakan connection string dari tab "Connection pooling"
   - Port: 6543 (bukan 5432)
   - Format: `postgresql://postgres.xxxxx:xxxxx@aws-0-xx-xxx.pooler.supabase.com:6543/postgres`

---

## 📊 Keuntungan Supabase

### ✅ Gratis:
- **500MB database** (cukup untuk development/testing)
- **Unlimited projects**
- **Auto-backup**
- **Real-time subscriptions**

### ✅ Fitur:
- **PostgreSQL database** (full SQL)
- **Auto-generated REST API**
- **Real-time subscriptions**
- **Storage** (untuk file uploads)
- **Authentication** (jika diperlukan)

### ✅ Monitoring:
- **Dashboard** untuk monitor database
- **Query logs**
- **Performance metrics**

---

## 🎯 Summary

### Setup Lengkap:
1. ✅ **Supabase:** Database (PostgreSQL 500MB gratis)
2. ✅ **Railway/Render:** Backend deployment (FastAPI)
3. ✅ **Connection:** Backend connect ke Supabase via `DATABASE_URL`

### Environment Variables yang Perlu:
```
DATABASE_URL=postgresql://postgres:PASSWORD@db.xxxxx.supabase.co:5432/postgres
JWT_SECRET=your-secret-key
API_HOST=0.0.0.0
API_PORT=8000 (atau 10000 untuk Render)
```

---

## 🔗 Links

- **Supabase:** https://supabase.com
- **Railway:** https://railway.app
- **Render:** https://render.com

---

## ✅ Checklist

- [ ] Buat akun Supabase
- [ ] Buat project baru
- [ ] Copy connection string
- [ ] Deploy backend ke Railway/Render
- [ ] Set environment variable `DATABASE_URL`
- [ ] Set environment variable `JWT_SECRET`
- [ ] Test health check
- [ ] Test register user
- [ ] Verifikasi tabel di Supabase

---

**Selamat! Database Supabase sudah terhubung dengan backend! 🚀**

