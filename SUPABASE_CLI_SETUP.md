# 🔧 Setup Database dengan Supabase CLI

Panduan lengkap untuk setup database menggunakan Supabase CLI dengan migration files.

---

## 📋 Prerequisites

1. **Node.js** terinstall (untuk Supabase CLI)
2. **Supabase project** sudah dibuat
3. **Supabase CLI** terinstall

---

## 🚀 Step 1: Install Supabase CLI

### Windows (PowerShell):

```powershell
# Install via npm
npm install -g supabase

# Atau via Scoop
scoop bucket add supabase https://github.com/supabase/scoop-bucket.git
scoop install supabase
```

### macOS (Homebrew):

```bash
brew install supabase/tap/supabase
```

### Linux:

```bash
npm install -g supabase
```

### Verify Installation:

```bash
supabase --version
```

---

## 🔐 Step 2: Login ke Supabase

```bash
supabase login
```

Ini akan membuka browser untuk login dengan akun Supabase Anda.

---

## 🔗 Step 3: Link Project

### Dapatkan Project Reference:

1. **Buka Supabase Dashboard:** https://supabase.com/dashboard
2. **Pilih project:** `jelantahgo-db`
3. **Settings → General → Reference ID**
4. **Copy Reference ID**

### Link Project:

```bash
supabase link --project-ref ybzzfgzzfrozxrujmjeo
```

**Ganti `ybzzfgzzfrozxrujmjeo` dengan Reference ID Anda jika berbeda.**

Atau gunakan connection string:

```bash
supabase link --db-url postgresql://postgres:jelantahgo-db@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres
```

---

## 📁 Step 4: Initialize Supabase (Jika Belum)

Jika belum ada folder `supabase`:

```bash
supabase init
```

Ini akan membuat folder `supabase/` dengan struktur:
```
supabase/
├── config.toml
└── migrations/
```

---

## 🗄️ Step 5: Run Migration

### Run Migration ke Supabase:

```bash
supabase db push
```

Atau:

```bash
supabase migration up
```

Ini akan menjalankan semua migration files di folder `supabase/migrations/` ke database Supabase.

---

## ✅ Step 6: Verify Migration

### Cek di Supabase Dashboard:

1. **Buka Supabase Dashboard**
2. **Table Editor**
3. **Pastikan tabel sudah ada:**
   - ✅ `users`
   - ✅ `customers`
   - ✅ `orders`
   - ✅ `billings`
   - ✅ `chat_messages`
   - ✅ `courier_locations`
   - ✅ `payment_proofs`

### Atau cek via CLI:

```bash
supabase db diff
```

---

## 🔄 Step 7: Deploy Aplikasi

Setelah migration selesai, deploy aplikasi:

### Railway:

1. **Deploy ke Railway**
2. **Set environment variables:**
   ```
   DATABASE_URL=postgresql://postgres:jelantahgo-db@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres
   JWT_SECRET=<generate-random-string>
   API_HOST=0.0.0.0
   API_PORT=8000
   ```
3. **Deploy**

### Render:

1. **Deploy ke Render**
2. **Set environment variables** (sama seperti Railway)
3. **Deploy**

---

## 📝 Migration File Structure

```
supabase/
├── config.toml          # Supabase configuration
└── migrations/
    └── 20240101000000_initial_schema.sql  # Initial schema migration
```

### Format Nama Migration:

```
YYYYMMDDHHMMSS_description.sql
```

Contoh:
- `20240101000000_initial_schema.sql`
- `20240102000000_add_indexes.sql`

---

## 🔧 Useful Commands

### Generate Migration dari Perubahan:

```bash
supabase db diff -f migration_name
```

### Reset Database:

```bash
supabase db reset
```

### Pull Schema dari Remote:

```bash
supabase db pull
```

### Check Migration Status:

```bash
supabase migration list
```

### Create New Migration:

```bash
supabase migration new migration_name
```

---

## 🆘 Troubleshooting

### Error: "project not found"

**Solusi:**
1. Pastikan Reference ID benar
2. Pastikan sudah login: `supabase login`
3. Coba link lagi dengan Reference ID yang benar

### Error: "connection refused"

**Solusi:**
1. Cek connection string
2. Pastikan password benar
3. Pastikan Supabase project masih aktif

### Error: "migration failed"

**Solusi:**
1. Cek syntax SQL di migration file
2. Pastikan tidak ada conflict dengan tabel yang sudah ada
3. Cek error message di Supabase dashboard → Logs

### Migration sudah dijalankan sebelumnya

**Solusi:**
1. Supabase CLI track migration history
2. Jika tabel sudah ada, migration akan skip
3. Atau reset database: `supabase db reset` (HATI-HATI: akan hapus semua data!)

---

## 📊 Workflow Lengkap

### Development:

1. **Install Supabase CLI**
2. **Login:** `supabase login`
3. **Link project:** `supabase link --project-ref <ref-id>`
4. **Edit migration files** di `supabase/migrations/`
5. **Run migration:** `supabase db push`
6. **Verify:** Cek di Supabase dashboard

### Production:

1. **Deploy aplikasi** (Railway/Render)
2. **Set DATABASE_URL**
3. **Aplikasi akan auto-create tables** (atau sudah dibuat via migration)

---

## ✅ Checklist

- [ ] Install Supabase CLI
- [ ] Login ke Supabase
- [ ] Link project
- [ ] Run migration: `supabase db push`
- [ ] Verify tables di Supabase dashboard
- [ ] Deploy aplikasi ke Railway/Render
- [ ] Set DATABASE_URL
- [ ] Test aplikasi

---

## 🎯 Keuntungan Supabase CLI

### ✅ Version Control:
- Migration files di Git
- Track perubahan schema
- Rollback jika perlu

### ✅ Consistency:
- Schema sama di semua environment
- Tidak perlu manual setup

### ✅ Team Collaboration:
- Semua developer pakai schema yang sama
- Migration history jelas

---

## 📚 Resources

- **Supabase CLI Docs:** https://supabase.com/docs/reference/cli
- **Migration Guide:** https://supabase.com/docs/guides/cli/local-development#database-migrations

---

## 💡 Tips

1. **Commit migration files ke Git:**
   ```bash
   git add supabase/migrations/
   git commit -m "Add initial database schema migration"
   ```

2. **Jangan edit migration yang sudah dijalankan:**
   - Buat migration baru untuk perubahan

3. **Test migration di local dulu:**
   ```bash
   supabase start  # Start local Supabase
   supabase db push  # Test migration
   ```

---

**Selamat! Database sudah di-setup dengan Supabase CLI! 🚀**

