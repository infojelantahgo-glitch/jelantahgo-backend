# 🔐 Supabase Environment Variables Setup

## ✅ Connection String (Lengkap)

```
DATABASE_URL=postgresql://postgres:jelantahgo-db@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres
```

---

## 🚂 Setup di Railway

### Step 1: Deploy ke Railway

1. **Buka [railway.app](https://railway.app)**
2. **New Project → Deploy from GitHub**
3. **Pilih:** `infojelantahgo-glitch/jelantahgo-backend`
4. **Railway akan otomatis deploy**

### Step 2: Setup Environment Variables

1. **Klik service yang baru dibuat**
2. **Tab "Variables"** (di sidebar)
3. **Klik "New Variable"** dan tambahkan:

   **Variable 1: DATABASE_URL**
   ```
   Key: DATABASE_URL
   Value: postgresql://postgres:jelantahgo-db@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres
   ```

   **Variable 2: JWT_SECRET**
   ```
   Key: JWT_SECRET
   Value: [generate dengan command di bawah]
   ```
   
   Generate JWT_SECRET:
   ```bash
   python -c "import secrets; print(secrets.token_urlsafe(32))"
   ```
   Copy hasilnya dan paste ke value.

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

### Step 3: Deploy

- Railway akan otomatis **redeploy** setelah environment variables ditambahkan
- Tunggu sampai status **"Deployed"** ✅

---

## 🎨 Setup di Render

### Step 1: Deploy ke Render

1. **Buka [render.com](https://render.com)**
2. **New → Web Service**
3. **Connect GitHub:** `infojelantahgo-glitch/jelantahgo-backend`
4. **Settings:**
   - Name: `jelantahgo-backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`
   - Plan: `Free`

### Step 2: Setup Environment Variables

1. **Tab "Environment"**
2. **Klik "Add Environment Variable"** dan tambahkan:

   **Variable 1: DATABASE_URL**
   ```
   Key: DATABASE_URL
   Value: postgresql://postgres:jelantahgo-db@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres
   ```

   **Variable 2: JWT_SECRET**
   ```
   Key: JWT_SECRET
   Value: [generate random string - lihat di bawah]
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
   Value: 10000
   ```
   (Render menggunakan port 10000, bukan 8000)

### Step 3: Deploy

- Render akan otomatis deploy
- Tunggu sampai status **"Live"** ✅

---

## ✅ Verifikasi Setup

### Test 1: Health Check

1. **Buka URL aplikasi:**
   - Railway: `https://your-app.up.railway.app/health`
   - Render: `https://your-app.onrender.com/health`

2. **Seharusnya return:**
   ```json
   {
     "status": "healthy",
     "service": "JelantahGO Backend"
   }
   ```

### Test 2: Database Connection

1. **Buka API docs:**
   - Railway: `https://your-app.up.railway.app/docs`
   - Render: `https://your-app.onrender.com/docs`

2. **Test register user:**
   - POST `/auth/register`
   - Body:
     ```json
     {
       "email": "test@example.com",
       "password": "test123",
       "role": "customer",
       "name": "Test User"
     }
     ```
   - Klik "Execute"
   - Jika berhasil (status 200), database connection OK! ✅

### Test 3: Cek Supabase Dashboard

1. **Buka:** https://supabase.com/dashboard
2. **Pilih project:** `jelantahgo-db`
3. **Table Editor** (di sidebar)
4. **Cek apakah tabel sudah dibuat:**
   - `users` ✅
   - `customers` ✅
   - `orders` ✅
   - `billings` ✅
   - `chat_messages` ✅
   - dll

---

## 🔒 Keamanan

### ⚠️ PENTING: Jangan Share Password!

- **Database password** (`jelantahgo-db`) adalah rahasia
- **Jangan commit** password ke GitHub
- **Gunakan environment variables** di Railway/Render
- **Jangan share** file ini yang berisi password

### Reset Password (jika diperlukan)

1. **Supabase Dashboard → Settings → Database**
2. **Database password → Reset database password**
3. **Update `DATABASE_URL`** di Railway/Render dengan password baru

---

## 📊 Environment Variables Summary

### Required Variables:

```env
DATABASE_URL=postgresql://postgres:jelantahgo-db@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres
JWT_SECRET=<generate-random-string>
API_HOST=0.0.0.0
API_PORT=8000  # atau 10000 untuk Render
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

## 🆘 Troubleshooting

### Error: "password authentication failed"

**Solusi:**
1. Pastikan password benar: `jelantahgo-db`
2. Cek format connection string
3. Pastikan tidak ada spasi di connection string

### Error: "could not connect to server"

**Solusi:**
1. Cek host: `db.ybzzfgzzfrozxrujmjeo.supabase.co`
2. Cek port: `5432`
3. Pastikan Supabase project masih aktif

### Error: "database does not exist"

**Solusi:**
- Database name di Supabase adalah `postgres` (bukan `jelantahgo-db`)
- Connection string sudah benar: `...:5432/postgres`

### Tabel tidak terbuat otomatis

**Solusi:**
1. Aplikasi akan otomatis membuat tabel saat pertama kali run
2. Atau jalankan manual:
   ```bash
   python init_db.py
   ```
   (Tapi ini untuk local, di Railway/Render akan otomatis)

---

## ✅ Checklist

- [ ] Deploy backend ke Railway/Render
- [ ] Set `DATABASE_URL` environment variable
- [ ] Set `JWT_SECRET` environment variable
- [ ] Set `API_HOST` environment variable
- [ ] Set `API_PORT` environment variable
- [ ] Test health check endpoint
- [ ] Test register user endpoint
- [ ] Verifikasi tabel di Supabase dashboard
- [ ] Test aplikasi lengkap

---

## 🎉 Selesai!

Setelah semua environment variables di-set, aplikasi akan:
- ✅ Connect ke Supabase database
- ✅ Create tables otomatis
- ✅ Siap digunakan!

**Aplikasi live di:**
- Railway: `https://your-app.up.railway.app`
- Render: `https://your-app.onrender.com`

**API Documentation:**
- `/docs` - Swagger UI
- `/redoc` - ReDoc

---

**Selamat! Database Supabase sudah terhubung! 🚀**

