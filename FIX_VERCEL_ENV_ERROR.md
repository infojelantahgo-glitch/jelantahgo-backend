# 🔧 Fix Vercel Environment Variable Error

## ❌ Error

```
Error: Environment Variable "DATABASE_URL" references Secret "database_url", which does not exist.
```

## ✅ Solution

**Problem:** `vercel.json` reference secret yang belum dibuat.

**Fix:** Removed env config dari `vercel.json`. Set environment variables manual setelah deploy.

---

## 🚀 Deploy Lagi

### Step 1: Deploy (tanpa env config)

```bash
vercel --prod
```

### Step 2: Set Environment Variables

**Option A: Via Vercel Dashboard (Recommended)**

1. Buka: https://vercel.com/dashboard
2. Pilih project: `jelantahgo-backend`
3. Settings → Environment Variables
4. Add variables:

   **DATABASE_URL:**
   ```
   postgresql://postgres.ybzzfgzzfrozxrujmjeo:jelantahgo-db@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres
   ```
   - Environment: Production, Preview, Development

   **JWT_SECRET:**
   ```
   FoJr8-mQNKJ-CX3R_xj5dKO1JGXbbEattsutJiIaA-s
   ```
   - Environment: Production, Preview, Development

   **API_HOST:**
   ```
   0.0.0.0
   ```
   - Environment: Production, Preview, Development

5. Redeploy setelah set variables

**Option B: Via CLI**

```bash
# Set DATABASE_URL
vercel env add DATABASE_URL production

# Input value:
# postgresql://postgres.ybzzfgzzfrozxrujmjeo:jelantahgo-db@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres

# Set JWT_SECRET
vercel env add JWT_SECRET production

# Input value:
# FoJr8-mQNKJ-CX3R_xj5dKO1JGXbbEattsutJiIaA-s

# Set API_HOST
vercel env add API_HOST production

# Input value:
# 0.0.0.0
```

---

## ✅ After Fix

1. ✅ `vercel.json` sudah di-fix (removed env config)
2. ⏳ Deploy lagi: `vercel --prod`
3. ⏳ Set environment variables (Dashboard atau CLI)
4. ⏳ Redeploy setelah set variables

---

## 🎯 Quick Commands

```bash
# Deploy
vercel --prod

# Set env via CLI
vercel env add DATABASE_URL production
vercel env add JWT_SECRET production
vercel env add API_HOST production

# Redeploy
vercel --prod
```

---

**🚀 Deploy lagi sekarang: `vercel --prod`**

