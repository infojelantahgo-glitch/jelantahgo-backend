# ⚡ Quick Start: Setup Supabase dengan CLI

Panduan cepat untuk setup database menggunakan Supabase CLI.

---

## 🚀 Langkah Cepat (5 Menit)

### 1. Install Supabase CLI

```bash
npm install -g supabase
```

### 2. Login

```bash
supabase login
```

### 3. Link Project

```bash
supabase link --project-ref ybzzfgzzfrozxrujmjeo
```

**Atau dengan connection string:**
```bash
supabase link --db-url postgresql://postgres:jelantahgo-db@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres
```

### 4. Run Migration

```bash
supabase db push
```

### 5. Verify

Buka Supabase Dashboard → Table Editor, pastikan tabel sudah ada:
- ✅ `users`
- ✅ `customers`
- ✅ `orders`
- ✅ `billings`
- ✅ `chat_messages`
- ✅ `courier_locations`
- ✅ `payment_proofs`

---

## ✅ Selesai!

Database sudah siap. Lanjutkan dengan deploy aplikasi ke Railway/Render.

---

## 📚 File Panduan Lengkap

- **SUPABASE_CLI_SETUP.md** - Panduan lengkap Supabase CLI
- **SUPABASE_ENV_SETUP.md** - Setup environment variables
- **SUPABASE_CONNECTION.md** - Info connection string

---

**Selamat! Database siap digunakan! 🚀**

