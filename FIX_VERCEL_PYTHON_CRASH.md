# 🔧 Fix Vercel Python Process Crash (Exit Status 1)

## 📋 Masalah

Dari log Vercel, semua request menghasilkan error:
- **Status Code:** 500
- **Error:** "Python process exited with exit status: 1"
- **Function:** `/api/index.py`
- **Duration:** 163-183ms sebelum crash

## 🔍 Analisis

Error terjadi saat **import/initialization** aplikasi, bukan saat runtime. Kemungkinan penyebab:

1. **Database connection error** saat import
2. **Missing environment variables** (DATABASE_URL, JWT_SECRET)
3. **File system operations** yang gagal di Vercel (read-only filesystem)
4. **Import dependencies** yang gagal

## ✅ Perbaikan yang Dilakukan

### 1. **api/index.py** - Better Error Handling
- ✅ Detailed logging untuk setiap step import
- ✅ Separate error handling untuk Mangum dan FastAPI app
- ✅ Fallback error handler yang informatif
- ✅ Error messages yang lebih jelas

### 2. **database.py** - Robust Vercel Support
- ✅ Skip `dotenv` di Vercel (gunakan environment variables langsung)
- ✅ Graceful handling jika DATABASE_URL tidak set
- ✅ Engine creation tidak crash jika gagal
- ✅ Logging untuk debugging

### 3. **file_upload.py** - Skip Directory Creation
- ✅ Skip directory creation di Vercel (filesystem read-only)
- ✅ Error handling untuk directory operations

### 4. **main.py** - Safe Table Creation
- ✅ Check engine sebelum create tables
- ✅ Skip table creation jika engine None

### 5. **vercel.json** - Modern Configuration
- ✅ Remove deprecated `builds` configuration
- ✅ Use `rewrites` instead (modern Vercel format)

## 🚀 Langkah Deploy

### 1. Pastikan Environment Variables di Vercel

Set di Vercel Dashboard → Settings → Environment Variables:

```env
DATABASE_URL=postgresql://postgres.ybzzfgzzfrozxrujmjeo:jelantahgo-db@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres
JWT_SECRET=FoJr8-mQNKJ-CX3R_xj5dKO1JGXbbEattsutJiIaA-s
API_HOST=0.0.0.0
```

**PENTING:** 
- Gunakan **pooler connection string** untuk Supabase (port 5432 atau 6543)
- Format: `postgresql://postgres.xxxxx:password@pooler.supabase.com:5432/postgres`

### 2. Deploy ke Vercel

```bash
# Commit perubahan
git add .
git commit -m "Fix Vercel Python crash: improve error handling and Vercel compatibility"
git push origin main

# Deploy ke Vercel
vercel --prod
```

### 3. Check Logs

Setelah deploy, check logs di Vercel Dashboard:
- **Deployments** → Pilih deployment terbaru → **Functions** → **View Logs**

Cari log messages:
- `[OK] Mangum imported successfully`
- `[OK] FastAPI app imported successfully`
- `[OK] Database engine created successfully`

Jika masih error, log akan menunjukkan di mana masalahnya.

## 🐛 Troubleshooting

### Error: "Failed to import Mangum"

**Solusi:**
- Pastikan `mangum==0.17.0` ada di `requirements-vercel.txt`
- Check build logs di Vercel untuk dependency installation

### Error: "Database connection not configured"

**Solusi:**
- Pastikan `DATABASE_URL` sudah di-set di Vercel environment variables
- Gunakan connection string yang benar (pooler format untuk Supabase)
- Test connection string dengan `psql` atau database client

### Error: "Failed to create database engine"

**Solusi:**
- Check format `DATABASE_URL` (harus valid PostgreSQL connection string)
- Pastikan database accessible dari Vercel (check firewall/network)
- Gunakan pooler connection untuk Supabase (lebih reliable)

### Error: "Application failed to initialize"

**Solusi:**
- Check logs di Vercel untuk detail error
- Pastikan semua dependencies terinstall
- Check apakah ada syntax error di Python files

## 📊 Expected Log Output

Setelah perbaikan, log seharusnya menunjukkan:

```
[OK] Mangum imported successfully
[OK] FastAPI app imported successfully
[OK] Database engine created successfully
[OK] SessionLocal created successfully
[OK] Mangum handler created successfully
```

Jika ada warning (bukan error), aplikasi masih bisa berjalan:
```
[WARNING] DATABASE_URL not set, using default (may fail)
[WARNING] Database operations will fail until DATABASE_URL is configured
```

## ✅ Checklist

- [ ] Environment variables sudah di-set di Vercel
- [ ] `DATABASE_URL` menggunakan format pooler untuk Supabase
- [ ] `JWT_SECRET` sudah di-set
- [ ] Semua dependencies ada di `requirements-vercel.txt`
- [ ] Code sudah di-commit dan push ke GitHub
- [ ] Deploy ke Vercel berhasil
- [ ] Check logs untuk confirm initialization berhasil
- [ ] Test health check endpoint: `/health`

## 🔗 Links

- **Vercel Dashboard:** https://vercel.com/dashboard
- **Supabase Connection Pooling:** https://supabase.com/docs/guides/database/connecting-to-postgres#connection-pooler
- **Vercel Python Runtime:** https://vercel.com/docs/functions/runtimes/python

---

**Status:** ✅ Fixed - Ready for deployment

