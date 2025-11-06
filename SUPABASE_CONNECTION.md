# 🔗 Supabase Connection String Setup

## 📋 Informasi yang Anda Punya:

- **Project URL:** https://ybzzfgzzfrozxrujmjeo.supabase.co
- **Database Name:** jelantahgo-db
- **Anon Key:** (ini untuk Supabase API, bukan untuk database connection)

---

## ✅ Yang Dibutuhkan: PostgreSQL Connection String

Untuk connect FastAPI ke Supabase database, kita perlu **PostgreSQL connection string**, bukan anon key.

---

## 🔧 Cara Dapatkan Connection String

### Step 1: Login ke Supabase Dashboard

1. **Buka:** https://supabase.com/dashboard
2. **Login** ke akun Anda
3. **Pilih project:** `jelantahgo-db`

### Step 2: Dapatkan Connection String

1. **Klik "Settings"** (ikon gear di sidebar kiri)
2. **Pilih "Database"** di menu
3. **Scroll ke bagian "Connection string"**
4. **Pilih tab "URI"**
5. **Copy connection string** yang formatnya seperti:

```
postgresql://postgres:[YOUR-PASSWORD]@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres
```

**PENTING:**
- Ganti `[YOUR-PASSWORD]` dengan password database yang Anda buat saat setup project
- Jika lupa password, bisa reset di: Settings → Database → Database password

### Step 3: Format Connection String yang Benar

**Format lengkap:**
```
postgresql://postgres:YOUR_PASSWORD@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres
```

**Contoh (ganti YOUR_PASSWORD dengan password Anda):**
```
postgresql://postgres:MyPassword123@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres
```

---

## 🚂 Setup di Railway

### Step 1: Deploy ke Railway

1. **Buka [railway.app](https://railway.app)**
2. **New Project → Deploy from GitHub**
3. **Pilih:** `infojelantahgo-glitch/jelantahgo-backend`

### Step 2: Setup Environment Variables

1. **Klik service yang baru dibuat**
2. **Tab "Variables"**
3. **Add Environment Variables:**

   **Variable 1: DATABASE_URL**
   ```
   Key: DATABASE_URL
   Value: postgresql://postgres:YOUR_PASSWORD@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres
   ```
   (Ganti `YOUR_PASSWORD` dengan password database Anda)

   **Variable 2: JWT_SECRET**
   ```
   Key: JWT_SECRET
   Value: [generate dengan command di bawah]
   ```
   
   Generate JWT_SECRET:
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

### Step 3: Deploy

- Railway akan otomatis redeploy
- Tunggu sampai status "Deployed"

---

## 🎨 Setup di Render

### Step 1: Deploy ke Render

1. **Buka [render.com](https://render.com)**
2. **New → Web Service**
3. **Connect GitHub:** `infojelantahgo-glitch/jelantahgo-backend`
4. **Settings:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`
   - Plan: `Free`

### Step 2: Setup Environment Variables

1. **Tab "Environment"**
2. **Add Environment Variables:**

   **Variable 1: DATABASE_URL**
   ```
   Key: DATABASE_URL
   Value: postgresql://postgres:YOUR_PASSWORD@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres
   ```

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
   (Render menggunakan port 10000)

---

## 🔒 Connection Pooling (Recommended untuk Production)

Supabase juga menyediakan **Connection Pooling** yang lebih efisien:

### Dapatkan Connection Pooling String

1. **Supabase Dashboard → Settings → Database**
2. **Tab "Connection pooling"**
3. **Copy connection string** (port 6543)

**Format:**
```
postgresql://postgres.ybzzfgzzfrozxrujmjeo:YOUR_PASSWORD@aws-0-xx-xxx.pooler.supabase.com:6543/postgres
```

**Gunakan connection pooling ini di production** untuk performa lebih baik!

---

## ✅ Verifikasi Connection

### Test Database Connection

1. **Buka URL aplikasi:**
   - Railway: `https://your-app.up.railway.app`
   - Render: `https://your-app.onrender.com`

2. **Test health check:**
   ```
   https://your-app-url/health
   ```

3. **Test register user:**
   - Buka: `https://your-app-url/docs`
   - POST `/auth/register`
   - Isi data user
   - Klik "Execute"
   - Jika berhasil, database connection OK!

### Cek di Supabase Dashboard

1. **Buka Supabase Dashboard**
2. **Table Editor**
3. **Cek apakah tabel sudah dibuat:**
   - `users`
   - `customers`
   - `orders`
   - `billings`
   - dll

---

## 🔐 Keamanan

### Jangan Share Password!

- **Database password** harus rahasia
- **Jangan commit** password ke GitHub
- **Gunakan environment variables** di Railway/Render

### Reset Password (jika lupa)

1. **Supabase Dashboard → Settings → Database**
2. **Database password → Reset database password**
3. **Update `DATABASE_URL`** di Railway/Render

---

## 📊 Summary

### Yang Sudah Punya:
- ✅ Project URL: https://ybzzfgzzfrozxrujmjeo.supabase.co
- ✅ Database Name: jelantahgo-db

### Yang Perlu:
- ⚠️ **Database Password** (password yang dibuat saat setup project)
- ⚠️ **Connection String** (dari Supabase Settings → Database)

### Connection String Format:
```
postgresql://postgres:YOUR_PASSWORD@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres
```

---

## 🆘 Troubleshooting

### Error: "password authentication failed"

**Solusi:**
1. Cek password di connection string
2. Reset password di Supabase: Settings → Database → Reset password
3. Update `DATABASE_URL` di Railway/Render

### Error: "could not connect to server"

**Solusi:**
1. Cek format connection string
2. Pastikan host benar: `db.ybzzfgzzfrozxrujmjeo.supabase.co`
3. Pastikan port: `5432` (atau `6543` untuk connection pooling)

### Error: "database does not exist"

**Solusi:**
- Database name di Supabase adalah `postgres` (bukan `jelantahgo-db`)
- Gunakan: `postgresql://...@host:5432/postgres`

---

## ✅ Checklist

- [ ] Dapatkan database password (atau reset jika lupa)
- [ ] Dapatkan connection string dari Supabase Dashboard
- [ ] Deploy backend ke Railway/Render
- [ ] Set `DATABASE_URL` environment variable
- [ ] Set `JWT_SECRET` environment variable
- [ ] Test health check
- [ ] Test register user
- [ ] Verifikasi tabel di Supabase

---

**Selamat! Database Supabase siap digunakan! 🚀**

