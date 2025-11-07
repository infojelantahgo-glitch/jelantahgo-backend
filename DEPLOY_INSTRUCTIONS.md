# 🚀 Instruksi Deploy ke Render

## ✅ Yang Sudah Disiapkan

1. ✅ Git repository sudah di-init
2. ✅ Semua file sudah di-commit
3. ✅ `main.py` sudah di-update untuk support Render port (10000)
4. ✅ File deployment config sudah ada:
   - `.github/workflows/deploy.yml` - GitHub Actions
   - `render.yaml` - Render config
   - `railway.json` - Railway config
   - `Procfile` - Process file

---

## 📤 Step 1: Push ke GitHub

### 1.1 Buat Repository di GitHub

1. Buka [github.com](https://github.com) dan login
2. Klik **"New repository"** (tombol hijau di pojok kanan)
3. Isi:
   - **Repository name:** `jelantahgo-backend` (atau nama lain)
   - **Description:** (opsional) "JelantahGO Backend API"
   - **Visibility:** Public atau Private (terserah)
   - **JANGAN centang** "Add a README file"
   - **JANGAN centang** "Add .gitignore"
   - **JANGAN centang** "Choose a license"
4. Klik **"Create repository"**

### 1.2 Connect dan Push

Copy dan jalankan command berikut di terminal (ganti `YOUR_USERNAME` dengan username GitHub Anda):

```bash
git remote add origin https://github.com/YOUR_USERNAME/jelantahgo-backend.git
git push -u origin main
```

**Contoh:**
```bash
git remote add origin https://github.com/nexag/jelantahgo-backend.git
git push -u origin main
```

Jika diminta login, gunakan:
- **Username:** username GitHub Anda
- **Password:** Personal Access Token (bukan password GitHub)
  - Cara buat token: GitHub → Settings → Developer settings → Personal access tokens → Generate new token
  - Centang scope: `repo`

---

## 🎨 Step 2: Deploy ke Render

### 2.1 Sign Up/Login Render

1. Buka [render.com](https://render.com)
2. Klik **"Get Started for Free"**
3. Login dengan **GitHub** (paling mudah)

### 2.2 Buat Web Service

1. Di dashboard Render, klik **"New +"** → **"Web Service"**
2. **Connect GitHub:**
   - Klik **"Connect account"** jika belum
   - Pilih repository **`jelantahgo-backend`**
   - Klik **"Connect"**
3. **Konfigurasi:**
   - **Name:** `jelantahgo-backend`
   - **Region:** Pilih yang terdekat (Singapore/US)
   - **Branch:** `main`
   - **Root Directory:** (kosongkan)
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python main.py`
   - **Plan:** `Free`
4. **JANGAN klik "Create Web Service" dulu!**

### 2.3 Buat PostgreSQL Database (SEBELUM Web Service)

1. Di dashboard Render, klik **"New +"** → **"PostgreSQL"**
2. **Konfigurasi:**
   - **Name:** `jelantahgo-db`
   - **Database:** `jelantahgo_db`
   - **User:** `jelantahgo`
   - **Region:** Sama dengan Web Service
   - **PostgreSQL Version:** `14` (atau terbaru)
   - **Plan:** `Free`
3. Klik **"Cr**eate Database"
4. **PENTING:** Copy **"Internal Database URL"** (akan digunakan nanti)
   - Format: `postgresql://jelantahgo:xxxxx@dpg-xxxxx/jelantahgo_db`

### 2.4 Kembali ke Web Service

1. Klik **"New +"** → **"Web Service"** lagi
2. Conne
3. **Environment Variables** (klik "Advancedct repository yang sama"):
   - Klik **"Add Environment Variable"**
   - Tambahkan satu per satu:
     
     **Variable 1:**
     - Key: `DATABASE_URL`
     - Value: (paste Internal Database URL dari PostgreSQL)
     
     **Variable 2:**
     - Key: `JWT_SECRET`
     - Value: (generate random string - lihat di bawah)
     
     **Variable 3:**
     - Key: `API_HOST`
     - Value: `0.0.0.0`
     
     **Variable 4:**
     - Key: `API_PORT`
     - Value: `10000`
     
     **Variable 5 (Opsional - untuk email):**
     - Key: `SMTP_HOST`
     - Value: `smtp.gmail.com`
     
     **Variable 6 (Opsional):**
     - Key: `SMTP_PORT`
     - Value: `587`
     
     **Variable 7 (Opsional):**
     - Key: `SMTP_USER`
     - Value: `your-email@gmail.com`
     
     **Variable 8 (Opsional):**
     - Key: `SMTP_PASSWORD`
     - Value: `your-app-password`
     
     **Variable 9 (Opsional):**
     - Key: `EMAIL_FROM`
     - Value: `your-email@gmail.com`

4. **Generate JWT_SECRET:**
   - Buka terminal dan jalankan:
     ```bash
     python -c "import secrets; print(secrets.token_urlsafe(32))"
     ```
   - Copy hasilnya ke environment variable `JWT_SECRET`

5. Klik **"Create Web Service"**

### 2.5 Tunggu Deploy

- Render akan otomatis:
  1. Clone repository dari GitHub
  2. Install dependencies (`pip install -r requirements.txt`)
  3. Run aplikasi (`python main.py`)
  4. Deploy ke internet

- Status akan berubah: **Building** → **Deploying** → **Live** ✅

---

## ✅ Step 3: Test Aplikasi

Setelah status **"Live"**, test aplikasi:

1. **Health Check:**
   ```
   https://jelantahgo-backend.onrender.com/health
   ```
   Seharusnya return:
   ```json
   {
     "status": "healthy",
     "service": "JelantahGO Backend"
   }
   ```

2. **API Documentation:**
   ```
   https://jelantahgo-backend.onrender.com/docs
   ```

3. **ReDoc:**
   ```
   https://jelantahgo-backend.onrender.com/redoc
   ```

---

## 🔧 Troubleshooting

### Deploy Gagal

1. **Cek Logs:**
   - Di Render dashboard → Web Service → **Logs**
   - Cari error message

2. **Common Errors:**
   - **Database connection error:** Pastikan `DATABASE_URL` benar
   - **Port error:** Pastikan `API_PORT=10000`
   - **Module not found:** Pastikan `requirements.txt` lengkap

### Aplikasi Sleep

- Render free tier sleep setelah 15 menit idle
- Wake up butuh ~30 detik saat pertama kali diakses
- Normal untuk free tier

### Database Error

- Pastikan PostgreSQL database sudah dibuat
- Pastikan `DATABASE_URL` menggunakan **Internal Database URL** (bukan External)
- Format: `postgresql://user:pass@host:port/db`

---

## 📝 Catatan Penting

1. **Port:** Render menggunakan port `10000` (bukan 8000)
2. **Database URL:** Gunakan **Internal Database URL** dari Render
3. **Cold Start:** Aplikasi butuh ~30 detik untuk wake up setelah sleep
4. **Free Tier Limit:** 750 jam/bulan (cukup untuk testing)

---

## 🎉 Selesai!

Setelah semua step selesai, aplikasi Anda akan live di:
```
https://jelantahgo-backend.onrender.com
```

**Selamat! Aplikasi sudah online! 🚀**

