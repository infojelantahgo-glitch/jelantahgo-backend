# 🔧 Fix 502 Bad Gateway Error

## ❌ Problem

Semua request mendapat **502 Bad Gateway** meskipun logs menunjukkan aplikasi sudah running.

**Error logs menunjukkan:**
```
Starting Container
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
[OK] Database tables created successfully!
```

Tapi semua request HTTP tetap dapat 502.

---

## 🔍 Root Cause

**Railway menggunakan `PORT` environment variable secara otomatis**, bukan `API_PORT`.

Railway set `PORT` variable secara otomatis untuk routing traffic. Jika aplikasi listen di port yang berbeda, Railway tidak bisa route traffic ke aplikasi.

---

## ✅ Solution

### Fix 1: Update main.py (ALREADY DONE)

Update `main.py` untuk menggunakan `PORT` environment variable dengan fallback ke `API_PORT` atau `8000`:

```python
if __name__ == "__main__":
    import os
    host = os.getenv("API_HOST", "0.0.0.0")
    # Railway uses PORT env var, fallback to API_PORT or 8000
    port = int(os.getenv("PORT", os.getenv("API_PORT", 8000)))
    uvicorn.run(app, host=host, port=port)
```

### Fix 2: Verify Railway Variables

Railway akan otomatis set `PORT` variable. Tidak perlu set manual.

Cek dengan:
```bash
railway variables --service jelantahgo-backend
```

Anda akan melihat `PORT` variable sudah ada (set oleh Railway).

---

## 🚀 After Fix

1. **Redeploy:**
   ```bash
   railway up --service jelantahgo-backend --detach
   ```

2. **Wait 1-2 minutes** untuk deployment selesai

3. **Test:**
   ```
   https://jelantahgo-backend-production.up.railway.app/health
   ```

4. **Expected:** JSON response, bukan 502

---

## 📋 Railway Port Configuration

### How Railway Works:

1. **Railway automatically assigns a port** and sets `PORT` environment variable
2. **Application must listen on `PORT`** for Railway to route traffic
3. **Railway routes external traffic** (port 443/80) to your application's `PORT`

### Environment Variables:

- `PORT` - Set automatically by Railway (DO NOT set manually)
- `API_HOST` - Set to `0.0.0.0` (already correct)
- `API_PORT` - Not used by Railway (only for local development)

---

## ✅ Verification

After redeploy, check:

1. **Logs should show:**
   ```
   INFO:     Uvicorn running on http://0.0.0.0:<PORT>
   ```
   (PORT adalah angka yang Railway set)

2. **Health check should work:**
   ```bash
   curl https://jelantahgo-backend-production.up.railway.app/health
   ```
   Expected: `{"status": "healthy", "service": "JelantahGO Backend"}`

3. **API docs should work:**
   ```
   https://jelantahgo-backend-production.up.railway.app/docs
   ```

---

## 🆘 If Still 502

### Check 1: Railway Dashboard

1. **Open:** https://railway.app/dashboard
2. **Select:** `jelantahgo-backend` service
3. **Check:**
   - Tab "Deployments" → Status should be "Active"
   - Tab "Logs" → Check for errors
   - Tab "Variables" → Verify `PORT` exists (auto-set by Railway)

### Check 2: Logs

```bash
railway logs --service jelantahgo-backend --tail 50
```

Look for:
- ✅ `INFO:     Uvicorn running on http://0.0.0.0:<PORT>`
- ❌ Any error messages

### Check 3: Force Redeploy

```bash
railway up --service jelantahgo-backend --detach
```

Wait 2-3 minutes, then test again.

---

## 📝 Summary

**Problem:** Aplikasi listen di port yang salah (8000) instead of Railway's PORT

**Solution:** Update `main.py` to use `PORT` env var (with fallback)

**Status:** ✅ Fixed - Redeploy needed

---

**After redeploy, aplikasi should work! 🚀**

