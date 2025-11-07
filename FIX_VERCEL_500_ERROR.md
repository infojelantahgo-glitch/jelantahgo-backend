# 🔧 Fix Vercel 500 Error - FUNCTION_INVOCATION_FAILED

## ❌ Error

```
500: INTERNAL_SERVER_ERROR
Code: FUNCTION_INVOCATION_FAILED
```

## 🔍 Root Causes

1. **Database table creation saat import** - Gagal di serverless environment
2. **Static files mounting** - Tidak support di serverless
3. **Environment variables belum di-set** - Database connection gagal
4. **Path issues** - Uploads directory tidak ada di serverless

## ✅ Fixes Applied

### 1. Skip Database Table Creation di Vercel

```python
# Skip in serverless environment
if not os.getenv("VERCEL"):
    models.Base.metadata.create_all(bind=engine)
```

### 2. Skip Static Files Mounting di Vercel

```python
# Skip in serverless environment
if not os.getenv("VERCEL"):
    app.mount("/files", StaticFiles(directory="uploads"), name="files")
```

### 3. Set VERCEL Environment Variable

```python
os.environ["VERCEL"] = "1"
```

### 4. Updated Mangum Handler

```python
handler = Mangum(app, lifespan="off")
```

---

## 🚀 Redeploy

### Step 1: Commit Changes

```bash
git add .
git commit -m "Fix Vercel serverless compatibility"
git push
```

### Step 2: Redeploy

```bash
vercel --prod
```

### Step 3: Set Environment Variables (CRITICAL!)

**Di Vercel Dashboard:**
1. Settings → Environment Variables
2. Add:
   - `DATABASE_URL`
   - `JWT_SECRET`
   - `API_HOST`

---

## ⚠️ Important Notes

### 1. Database Tables

**Table creation skipped di Vercel.** Pastikan tables sudah dibuat:
- ✅ Di Supabase Dashboard (SQL Editor)
- ✅ Atau di Railway (sudah dibuat otomatis)

### 2. File Uploads

**Static files tidak support di Vercel serverless.**

**Solutions:**
- ✅ Use external storage (S3, Cloudinary, Supabase Storage)
- ✅ Or keep backend di Railway untuk file uploads

### 3. Environment Variables

**MUST SET di Vercel Dashboard:**
- `DATABASE_URL` - Required!
- `JWT_SECRET` - Required!
- `API_HOST` - Optional

---

## 🎯 Recommended Solution

**Untuk backend FastAPI dengan file uploads:**

1. **Keep backend di Railway** (sudah working) ✅
   - URL: https://jelantahgo-backend-production.up.railway.app
   - Support file uploads
   - Support database table creation
   - Better for long-running processes

2. **Use Vercel untuk frontend** ✅
   - Connect ke backend di Railway
   - Perfect untuk React/Next.js/Vue

---

## 📋 After Fix

1. ✅ Code updated untuk serverless compatibility
2. ⏳ Commit & push changes
3. ⏳ Redeploy ke Vercel
4. ⏳ Set environment variables
5. ⏳ Test endpoints

---

**🚀 Fix sudah applied! Commit, push, dan redeploy!**

