# 🚀 Deploy via Railway Dashboard (Lebih Mudah)

Karena Railway CLI butuh beberapa setup, deploy via Dashboard lebih mudah!

---

## ✅ Step 1: Buka Railway Dashboard

1. **Buka:** https://railway.app/dashboard
2. **Login** dengan GitHub (jika belum)
3. **Pilih project:** `jelantahgo-backend`

---

## ✅ Step 2: Connect GitHub Repository

1. **Klik "New"** (tombol + di pojok kiri bawah)
2. **Pilih "GitHub Repo"**
3. **Pilih repository:** `infojelantahgo-glitch/jelantahgo-backend`
4. **Railway akan otomatis:**
   - Detect Python project
   - Install dependencies
   - Deploy aplikasi

---

## ✅ Step 3: Setup Environment Variables

1. **Klik service yang baru dibuat**
2. **Tab "Variables"** (di sidebar)
3. **Klik "New Variable"** dan tambahkan:

   ```
   DATABASE_URL = postgresql://postgres:jelantahgo-db@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres
   JWT_SECRET = FoJr8-mQNKJ-CX3R_xj5dKO1JGXbbEattsutJiIaA-s
   API_HOST = 0.0.0.0
   API_PORT = 8000
   ```

4. **Railway akan otomatis redeploy** setelah variables di-set

---

## ✅ Step 4: Verify Deployment

1. **Tab "Deployments"**
2. **Tunggu sampai status "Active"**
3. **Klik domain** atau copy URL deployment
4. **Test:**
   - Health check: `https://your-app.up.railway.app/health`
   - API docs: `https://your-app.up.railway.app/docs`

---

## ✅ Step 5: Cek Logs

1. **Tab "Logs"**
2. **Cari:** `[OK] Database tables created successfully!`
3. **Pastikan tidak ada error**

---

## 🎯 Quick Summary

1. Dashboard → New → GitHub Repo
2. Pilih: `infojelantahgo-glitch/jelantahgo-backend`
3. Set environment variables
4. Tunggu deploy selesai
5. Test aplikasi

---

**Lebih mudah via Dashboard! 🚀**

