# 🔧 Fix Supabase Connection Issue

## ❌ Error yang Terjadi

```
Network is unreachable
connection to server at "db.ybzzfgzzfrozxrujmjeo.supabase.co" (2406:da18:243:741b:6849:8e34:4bd5:fb40), port 5432 failed
```

## 🔍 Penyebab

Railway tidak bisa connect ke Supabase karena:
1. **IPv6 issue**: Railway mencoba connect via IPv6, tapi mungkin Supabase belum support atau perlu setup khusus
2. **Connection Pooler**: Supabase punya **Connection Pooler** yang lebih reliable untuk external connections
3. **Database Settings**: Supabase database mungkin perlu di-enable untuk external connections

---

## ✅ Solusi 1: Gunakan Connection Pooler (RECOMMENDED)

Supabase punya **Connection Pooler** yang lebih reliable untuk connections dari cloud providers.

### Langkah:

1. **Buka Supabase Dashboard:**
   - https://supabase.com/dashboard/project/ybzzfgzzfrozxrujmjeo/settings/database

2. **Copy Connection Pooler URL:**
   - Scroll ke bagian **"Connection Pooling"**
   - Copy **"Connection string"** (bukan direct connection)
   - Format: `postgresql://postgres.[project-ref]:[password]@aws-0-[region].pooler.supabase.com:6543/postgres`

3. **Update Railway Variable:**
   ```bash
   railway variables --set "DATABASE_URL=<CONNECTION_POOLER_URL>" --service jelantahgo-backend
   ```

4. **Redeploy:**
   ```bash
   railway up --service jelantahgo-backend
   ```

---

## ✅ Solusi 2: Enable IPv4 Only (Alternative)

Jika Connection Pooler tidak tersedia, kita bisa force IPv4:

1. **Buka Supabase Dashboard:**
   - Settings → Database → Connection Pooling

2. **Gunakan port 6543** (pooler port) atau **5432 dengan IPv4**

3. **Update DATABASE_URL** dengan menambahkan `?options=-c%20ip_family=ipv4`

---

## ✅ Solusi 3: Check Supabase Database Settings

1. **Buka:** https://supabase.com/dashboard/project/ybzzfgzzfrozxrujmjeo/settings/database

2. **Cek:**
   - ✅ **"Database"** status harus **Active**
   - ✅ **"Connection pooling"** harus **Enabled**
   - ✅ **"Direct connections"** harus **Allowed**

3. **Jika belum enabled, enable dulu**

---

## ✅ Solusi 4: Pilih Mode Pooler yang Tepat

Supabase Connection Pooler punya 2 mode:

### 🎯 **SESSION POOLER** (RECOMMENDED untuk FastAPI + Railway)

**Kenapa Session Pooler?**
- ✅ **SQLAlchemy** menggunakan session-based connections (`SessionLocal`)
- ✅ **Railway** adalah containerized app (long-running), bukan serverless
- ✅ **Support prepared statements** (SQLAlchemy memanfaatkan ini untuk performa)
- ✅ **Cocok untuk aplikasi stateful** dengan multiple queries per request

**Session Pooler URL:**
```
postgresql://postgres.[project-ref]:[password]@aws-0-[region].pooler.supabase.com:6543/postgres
```
- Port: **6543** (pooler)
- **TANPA** parameter `?pgbouncer=true`

### ⚡ **TRANSACTION POOLER** (Alternatif untuk Troubleshooting)

**Kapan pakai Transaction Pooler?**
- ⚠️ Jika Session Pooler masih error
- ⚠️ Untuk testing koneksi
- ⚠️ Jika aplikasi benar-benar stateless (tapi FastAPI + SQLAlchemy biasanya tidak)

**Transaction Pooler URL:**
```
postgresql://postgres.[project-ref]:[password]@aws-0-[region].pooler.supabase.com:6543/postgres?pgbouncer=true
```
- Port: **6543** (pooler)
- **DENGAN** parameter `?pgbouncer=true`

---

### 💡 **REKOMENDASI: SESSION POOLER**

Untuk FastAPI + SQLAlchemy di Railway, **gunakan SESSION POOLER** (tanpa `?pgbouncer=true`).

---

## 🚀 Quick Fix (Step-by-Step)

### Step 1: Dapatkan Connection Pooler URL

1. Buka: https://supabase.com/dashboard/project/ybzzfgzzfrozxrujmjeo/settings/database
2. Scroll ke **"Connection Pooling"**
3. Copy **"Connection string"** (bukan "Direct connection")

### Step 2: Update Railway

```bash
railway variables --set "DATABASE_URL=<POOLER_URL>" --service jelantahgo-backend
```

### Step 3: Redeploy

```bash
railway up --service jelantahgo-backend --detach
```

### Step 4: Check Logs

```bash
railway logs --service jelantahgo-backend --tail 30
```

---

## 📋 Checklist

- [ ] Connection Pooler enabled di Supabase
- [ ] DATABASE_URL menggunakan pooler URL (port 6543)
- [ ] Railway variables sudah di-update
- [ ] Redeploy sudah dilakukan
- [ ] Logs menunjukkan koneksi berhasil

---

**Masih error?** Cek:
- Supabase project status
- Railway network settings
- Firewall rules

