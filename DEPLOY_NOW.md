# 🚀 DEPLOY KE VERCEL SEKARANG

## ✅ Files Sudah Disiapkan

- ✅ `api/index.py` - Vercel serverless function (dengan Mangum)
- ✅ `vercel.json` - Vercel config untuk Python
- ✅ `requirements-vercel.txt` - Dependencies (termasuk Mangum)

---

## 🚀 Langkah Deploy

### 1. Login ke Vercel

```bash
vercel login
```

### 2. Deploy

```bash
vercel --prod
```

### 3. Set Environment Variables

Setelah deploy, set di Vercel Dashboard:

**DATABASE_URL:**
```
postgresql://postgres.ybzzfgzzfrozxrujmjeo:jelantahgo-db@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres
```

**JWT_SECRET:**
```
FoJr8-mQNKJ-CX3R_xj5dKO1JGXbbEattsutJiIaA-s
```

**API_HOST:**
```
0.0.0.0
```

---

## ⚠️ Catatan Penting

1. **Serverless Functions:**
   - Ada cold start delay
   - Database connection pooling perlu di-adjust

2. **File Upload:**
   - Perlu external storage (Vercel storage atau S3)

3. **Backend di Railway (Recommended):**
   - https://jelantahgo-backend-production.up.railway.app
   - Lebih cocok untuk backend!

---

## 🎯 Quick Commands

```bash
# Login
vercel login

# Deploy
vercel --prod

# Set env (via CLI)
vercel env add DATABASE_URL production
vercel env add JWT_SECRET production
```

---

**🚀 Jalankan: `vercel login` lalu `vercel --prod`!**
