# 🚀 Alternatif Platform Deploy (Selain Render)

Berikut adalah platform alternatif untuk deploy aplikasi JelantahGO Backend:

---

## 1. 🚂 Railway (Recommended - Paling Mudah)

### ✅ Kelebihan:
- **Gratis:** $5 credit saat sign up
- **Auto-deploy dari GitHub**
- **PostgreSQL included**
- **Tidak perlu kartu kredit** (untuk mulai)
- **Domain gratis:** `your-app.up.railway.app`
- **SSL/HTTPS gratis**

### 📋 Cara Setup:

1. **Buka [railway.app](https://railway.app)**
2. **Sign up dengan GitHub** (gratis)
3. **New Project → Deploy from GitHub repo**
4. **Pilih repository:** `infojelantahgo-glitch/jelantahgo-backend`
5. **Railway otomatis:**
   - Detect Python
   - Install dependencies
   - Deploy aplikasi

### 🔧 Setup Database:

1. Di project → **New → Database → PostgreSQL**
2. Railway otomatis set `DATABASE_URL` environment variable
3. Tidak perlu setup manual!

### 💰 Pricing:
- **Free:** $5 credit (cukup untuk testing)
- **Pay-as-you-go:** Setelah credit habis (~$0.01/jam)

**File config sudah ada:** `railway.json` ✅

---

## 2. 🐳 Fly.io (Free Tier Available)

### ✅ Kelebihan:
- **Gratis:** 3 shared-cpu VMs gratis
- **PostgreSQL gratis** (3GB storage)
- **Global deployment**
- **Custom domain gratis**

### 📋 Cara Setup:

1. **Install Fly CLI:**
   ```bash
   # Windows (PowerShell)
   iwr https://fly.io/install.ps1 -useb | iex
   ```

2. **Login:**
   ```bash
   fly auth login
   ```

3. **Deploy:**
   ```bash
   fly launch
   ```

4. **Setup PostgreSQL:**
   ```bash
   fly postgres create --name jelantahgo-db
   fly postgres attach jelantahgo-db
   ```

### 💰 Pricing:
- **Free:** 3 shared-cpu VMs, 3GB PostgreSQL
- **Hobby:** $1.94/month per VM

**Website:** [fly.io](https://fly.io)

---

## 3. ☁️ Render (Yang Sudah Dicoba)

### ✅ Kelebihan:
- **Gratis:** 750 jam/bulan
- **Tidak perlu kartu kredit**
- **PostgreSQL gratis** (90MB)
- **Auto-deploy dari GitHub**

### ❌ Kekurangan:
- App sleep setelah 15 menit idle
- Kadang ada masalah saat buat PostgreSQL

**File config sudah ada:** `render.yaml` ✅

---

## 4. 🟣 Supabase (Backend + Database)

### ✅ Kelebihan:
- **Gratis:** Unlimited projects
- **PostgreSQL gratis** (500MB)
- **Auto-backup**
- **API management included**

### 📋 Cara Setup:

1. **Buka [supabase.com](https://supabase.com)**
2. **New Project**
3. **Copy PostgreSQL connection string**
4. **Deploy backend di Railway/Render**
5. **Gunakan Supabase database**

### 💰 Pricing:
- **Free:** 500MB database, unlimited projects
- **Pro:** $25/month

---

## 5. 🌐 Vercel (Untuk API)

### ✅ Kelebihan:
- **Gratis:** Unlimited deployments
- **Auto-deploy dari GitHub**
- **Edge functions**
- **CDN included**

### 📋 Cara Setup:

1. **Buka [vercel.com](https://vercel.com)**
2. **Import GitHub repository**
3. **Framework Preset:** Other
4. **Build Command:** `pip install -r requirements.txt`
5. **Output Directory:** (kosongkan)
6. **Install Command:** (kosongkan)

**Note:** Vercel lebih cocok untuk serverless. Untuk full FastAPI app, lebih baik Railway/Render.

---

## 6. 🐘 ElephantSQL (PostgreSQL Hosting)

### ✅ Kelebihan:
- **Gratis:** 20MB database
- **Dedicated PostgreSQL**
- **Easy setup**

### 📋 Cara Setup:

1. **Buka [elephantsql.com](https://elephantsql.com)**
2. **Sign up**
3. **Create Instance → Tiny Turtle (Free)**
4. **Copy connection string**
5. **Gunakan di Railway/Render sebagai DATABASE_URL**

### 💰 Pricing:
- **Free:** 20MB (cukup untuk testing)
- **Paid:** Mulai dari $19/month

---

## 7. 🖥️ VPS Sendiri (Full Control)

### ✅ Kelebihan:
- **Full control**
- **Custom domain**
- **Tidak ada limit**
- **Lebih murah untuk production**

### 📋 Platform VPS:
- **DigitalOcean:** $4/month (droplet)
- **Vultr:** $2.50/month (starter)
- **Linode:** $5/month
- **Hetzner:** €4/month

### 📋 Cara Setup:
Lihat file `DEPLOYMENT.md` section "VPS (Ubuntu/Debian)"

**File script sudah ada:** `deploy.sh` ✅

---

## 📊 Perbandingan Platform

| Platform | Free Tier | Database | Auto-Deploy | Rekomendasi |
|----------|-----------|----------|-------------|-------------|
| **Railway** | $5 credit | ✅ Included | ✅ | ⭐⭐⭐⭐⭐ |
| **Render** | 750 jam/bulan | ✅ Free (90MB) | ✅ | ⭐⭐⭐⭐ |
| **Fly.io** | 3 VMs | ✅ Free (3GB) | ✅ | ⭐⭐⭐⭐ |
| **Supabase** | Unlimited | ✅ Free (500MB) | ❌ | ⭐⭐⭐⭐ |
| **Vercel** | Unlimited | ❌ (External) | ✅ | ⭐⭐⭐ |
| **ElephantSQL** | 20MB | ✅ Free | ❌ | ⭐⭐⭐ |
| **VPS** | ❌ | Manual | Manual | ⭐⭐⭐⭐ |

---

## 🎯 Rekomendasi Berdasarkan Kebutuhan

### Untuk Development/Testing:
1. **Railway** (paling mudah, $5 credit)
2. **Render** (gratis, tapi ada masalah PostgreSQL)
3. **Fly.io** (gratis, lebih stabil)

### Untuk Production:
1. **Railway** (pay-as-you-go, murah)
2. **VPS** (full control, lebih murah)
3. **Render** (paid plan)

### Untuk Database Saja:
1. **Supabase** (500MB gratis)
2. **Railway PostgreSQL** (included)
3. **ElephantSQL** (20MB gratis)

---

## 🚀 Quick Start: Railway (Recommended)

### Step 1: Sign Up
1. Buka [railway.app](https://railway.app)
2. Login dengan GitHub

### Step 2: Deploy
1. **New Project → Deploy from GitHub**
2. Pilih: `infojelantahgo-glitch/jelantahgo-backend`
3. Railway auto-detect dan deploy

### Step 3: Database
1. **New → Database → PostgreSQL**
2. Railway otomatis set `DATABASE_URL`
3. Selesai!

### Step 4: Environment Variables
Railway otomatis set:
- `DATABASE_URL` ✅
- Tambahkan manual:
  - `JWT_SECRET` = (generate random string)
  - `API_HOST` = `0.0.0.0`
  - `API_PORT` = `8000`

### Step 5: Done! 🎉
Aplikasi live di: `https://your-app.up.railway.app`

---

## 💡 Tips

1. **Railway** paling mudah untuk pemula
2. **Render** bagus jika tidak ada masalah
3. **Fly.io** bagus untuk production
4. **VPS** bagus untuk full control

---

## 🔗 Link Platform

- **Railway:** https://railway.app
- **Render:** https://render.com
- **Fly.io:** https://fly.io
- **Supabase:** https://supabase.com
- **Vercel:** https://vercel.com
- **ElephantSQL:** https://elephantsql.com

---

**Pilih platform yang paling sesuai dengan kebutuhan Anda! 🚀**

