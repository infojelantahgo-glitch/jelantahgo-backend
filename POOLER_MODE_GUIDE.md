# 🎯 Supabase Connection Pooler: Session vs Transaction Mode

## 📊 Perbandingan

| Aspek | Session Pooler | Transaction Pooler |
|-------|---------------|-------------------|
| **Port** | 6543 | 6543 |
| **Parameter URL** | - | `?pgbouncer=true` |
| **Prepared Statements** | ✅ Support | ❌ Tidak support |
| **Session State** | ✅ Maintained | ❌ Reset setiap transaksi |
| **Cocok untuk** | Long-running apps, ORM | Serverless, stateless |
| **Koneksi** | Eksklusif per client | Shared antar client |

---

## 🎯 Untuk FastAPI + SQLAlchemy + Railway

### ✅ **Gunakan SESSION POOLER** (RECOMMENDED)

**Alasan:**
1. **SQLAlchemy menggunakan sessions** (`SessionLocal`, `sessionmaker`)
2. **FastAPI dengan SQLAlchemy** membutuhkan prepared statements support
3. **Railway adalah containerized app** (long-running process), bukan serverless
4. **Multiple queries per request** membutuhkan session state

---

## 🔧 Setup Session Pooler

### Step 1: Dapatkan Session Pooler URL

1. **Buka Supabase Dashboard:**
   - https://supabase.com/dashboard/project/ybzzfgzzfrozxrujmjeo/settings/database

2. **Scroll ke "Connection Pooling"**

3. **Copy "Connection string"** (bukan "Transaction mode")
   - Format: `postgresql://postgres.[project-ref]:[password]@aws-0-[region].pooler.supabase.com:6543/postgres`
   - **TANPA** `?pgbouncer=true`

### Step 2: Update Railway Variable

```bash
railway variables --set "DATABASE_URL=<SESSION_POOLER_URL>" --service jelantahgo-backend
```

### Step 3: Redeploy

```bash
railway up --service jelantahgo-backend --detach
```

---

## ⚡ Setup Transaction Pooler (Alternatif)

Jika Session Pooler masih error, coba Transaction Pooler:

### Step 1: Dapatkan Transaction Pooler URL

1. **Buka Supabase Dashboard**
2. **Connection Pooling → Transaction mode**
3. **Copy Connection string**
   - Format: `postgresql://postgres.[project-ref]:[password]@aws-0-[region].pooler.supabase.com:6543/postgres?pgbouncer=true`
   - **DENGAN** `?pgbouncer=true`

### Step 2: Update Railway Variable

```bash
railway variables --set "DATABASE_URL=<TRANSACTION_POOLER_URL>" --service jelantahgo-backend
```

### Step 3: Update database.py (Opsional)

Jika menggunakan Transaction Pooler, mungkin perlu disable prepared statements:

```python
# database.py
engine = create_engine(
    DATABASE_URL,
    connect_args={"options": "-cstatement_timeout=30000"},
    pool_pre_ping=True  # Test connections before using
)
```

### Step 4: Redeploy

```bash
railway up --service jelantahgo-backend --detach
```

---

## 🔍 Cara Cek Mode di Supabase

1. **Buka:** https://supabase.com/dashboard/project/ybzzfgzzfrozxrujmjeo/settings/database
2. **Scroll ke "Connection Pooling"**
3. **Ada 2 tab:**
   - **"Session mode"** → Copy URL ini (RECOMMENDED)
   - **"Transaction mode"** → URL dengan `?pgbouncer=true` (Alternatif)

---

## ✅ Checklist

### Session Pooler (Recommended):
- [ ] Copy Session Pooler URL (tanpa `?pgbouncer=true`)
- [ ] Update `DATABASE_URL` di Railway
- [ ] Redeploy
- [ ] Test koneksi

### Transaction Pooler (Jika Session gagal):
- [ ] Copy Transaction Pooler URL (dengan `?pgbouncer=true`)
- [ ] Update `DATABASE_URL` di Railway
- [ ] Update `database.py` jika perlu (disable prepared statements)
- [ ] Redeploy
- [ ] Test koneksi

---

## 🚀 Quick Decision

**Untuk aplikasi ini (FastAPI + SQLAlchemy + Railway):**

👉 **Gunakan SESSION POOLER** (tanpa `?pgbouncer=true`)

**URL Format:**
```
postgresql://postgres.ybzzfgzzfrozxrujmjeo:jelantahgo-db@aws-0-xx-xxx.pooler.supabase.com:6543/postgres
```

---

**Lebih detail?** Cek `FIX_SUPABASE_CONNECTION.md`

