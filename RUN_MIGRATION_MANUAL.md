# 🚀 Cara Run Migration ke Supabase (Manual)

Karena Supabase CLI perlu interaksi browser untuk login, ada beberapa cara alternatif untuk run migration:

---

## ✅ Metode 1: Via Supabase Dashboard SQL Editor (Paling Mudah)

### Step 1: Buka Supabase SQL Editor

1. **Buka:** https://supabase.com/dashboard
2. **Login** ke akun Supabase
3. **Pilih project:** `jelantahgo-db`
4. **Klik "SQL Editor"** di sidebar kiri
5. **Klik "New query"**

### Step 2: Copy-Paste Migration SQL

1. **Buka file:** `supabase/migrations/20240101000000_initial_schema.sql`
2. **Copy semua isi file**
3. **Paste di SQL Editor**
4. **Klik "Run"** (atau tekan Ctrl+Enter)

### Step 3: Verify

1. **Klik "Table Editor"** di sidebar
2. **Pastikan tabel sudah ada:**
   - ✅ `users`
   - ✅ `customers`
   - ✅ `orders`
   - ✅ `billings`
   - ✅ `chat_messages`
   - ✅ `courier_locations`
   - ✅ `payment_proofs`

---

## ✅ Metode 2: Via Supabase CLI (Butuh Login Manual)

### Step 1: Login (Jalankan di Terminal)

```bash
npx supabase login
```

Ini akan membuka browser untuk login. Setelah login berhasil, lanjutkan ke step 2.

### Step 2: Link Project

```bash
npx supabase link --project-ref ybzzfgzzfrozxrujmjeo --password jelantahgo-db
```

### Step 3: Run Migration

```bash
npx supabase db push
```

---

## ✅ Metode 3: Via psql (Jika Terinstall)

### Step 1: Install psql (jika belum)

Download dari: https://www.postgresql.org/download/windows/

### Step 2: Run Migration

```bash
psql "postgresql://postgres:jelantahgo-db@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres" -f supabase/migrations/20240101000000_initial_schema.sql
```

---

## ✅ Metode 4: Auto-Create via Aplikasi (Recommended)

**TIDAK PERLU run migration manual!**

Aplikasi akan **otomatis create tables** saat pertama kali run:

1. **Deploy aplikasi ke Railway/Render**
2. **Set `DATABASE_URL` environment variable**
3. **Aplikasi akan auto-create semua tabel** (via SQLAlchemy)
4. **Cek logs:** `[OK] Database tables created successfully!`

**Ini cara termudah dan recommended!**

---

## 🎯 Rekomendasi

### Untuk Development/Testing:
**Gunakan Metode 1 (Supabase Dashboard SQL Editor)**
- ✅ Paling mudah
- ✅ Tidak perlu install apapun
- ✅ Bisa lihat hasil langsung

### Untuk Production:
**Gunakan Metode 4 (Auto-create via aplikasi)**
- ✅ Otomatis
- ✅ Konsisten dengan models.py
- ✅ Tidak perlu manual setup

---

## 📋 Checklist

- [ ] Pilih metode (1, 2, 3, atau 4)
- [ ] Run migration (atau deploy aplikasi)
- [ ] Verify tables di Supabase dashboard
- [ ] Deploy aplikasi (jika belum)
- [ ] Test aplikasi

---

## 🔍 Verify Migration

Setelah migration, cek di Supabase:

1. **Dashboard → Table Editor**
2. **Pastikan 7 tabel sudah ada:**
   - `users`
   - `customers`
   - `orders`
   - `billings`
   - `chat_messages`
   - `courier_locations`
   - `payment_proofs`

---

**Selamat! Database siap digunakan! 🚀**

