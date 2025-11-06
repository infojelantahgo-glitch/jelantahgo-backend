# 🔧 Fix: Tabel Indonesia vs Inggris

## ⚠️ Masalah yang Ditemukan

Di Supabase dashboard, ada tabel dengan nama **bahasa Indonesia**:
- `pengguna` (seharusnya `users`)
- `pelanggan` (seharusnya `customers`)
- `pesanan` (seharusnya `orders`)
- `tagihan` (seharusnya `billings`)
- `pesan_obrolan` (seharusnya `chat_messages`)
- `lokasi_kurir` (seharusnya `courier_locations`)
- `bukti_pembayaran` (seharusnya `payment_proofs`)

**Aplikasi ini menggunakan nama tabel dalam bahasa Inggris** (sesuai `models.py`).

---

## ✅ Solusi

### Opsi 1: Rename Tabel Indonesia ke Inggris (Jika Ada Data Penting)

Jika tabel Indonesia sudah berisi data penting:

1. **Buka Supabase SQL Editor**
2. **Copy isi file:** `supabase/migrations/20240101000001_rename_tables_to_english.sql`
3. **Paste dan Run**

Script akan rename tabel Indonesia ke Inggris.

### Opsi 2: Drop Tabel Indonesia (Jika Tidak Ada Data Penting)

Jika tabel Indonesia tidak berisi data penting atau ingin mulai fresh:

1. **Buka Supabase SQL Editor**
2. **Copy isi file:** `supabase/migrations/20240101000002_drop_indonesian_tables.sql`
3. **Paste dan Run**

**HATI-HATI:** Script ini akan HAPUS semua data di tabel Indonesia!

### Opsi 3: Biarkan, Aplikasi Akan Buat Tabel Baru (Recommended)

**TIDAK PERLU DO APAPUN!**

Aplikasi akan otomatis create tabel baru dengan nama Inggris saat pertama kali run. Tabel Indonesia akan tetap ada tapi tidak digunakan.

---

## 🎯 Rekomendasi

### Jika Tabel Indonesia Kosong/Tidak Penting:
**Gunakan Opsi 2 (Drop tabel Indonesia)**, lalu:
1. Run migration: `supabase/migrations/20240101000000_initial_schema.sql`
2. Atau deploy aplikasi (akan auto-create)

### Jika Tabel Indonesia Berisi Data Penting:
**Gunakan Opsi 1 (Rename tabel)**, lalu verifikasi struktur kolom sesuai.

### Jika Tidak Yakin:
**Gunakan Opsi 3 (Biarkan, aplikasi akan create tabel baru)**:
- Aplikasi akan create tabel Inggris saat deploy
- Tabel Indonesia tetap ada (tidak digunakan)
- Bisa dihapus manual nanti jika tidak diperlukan

---

## 📋 Mapping Tabel

| Indonesia (Lama) | Inggris (Baru) | Status |
|-----------------|----------------|--------|
| `pengguna` | `users` | Perlu rename/create |
| `pelanggan` | `customers` | Perlu rename/create |
| `pesanan` | `orders` | Perlu rename/create |
| `tagihan` | `billings` | Perlu rename/create |
| `pesan_obrolan` | `chat_messages` | Perlu rename/create |
| `lokasi_kurir` | `courier_locations` | Perlu rename/create |
| `bukti_pembayaran` | `payment_proofs` | Perlu rename/create |

---

## 🚀 Quick Fix (Via SQL Editor)

### Rename Tabel (Jika Ada Data):

```sql
-- Copy dari: supabase/migrations/20240101000001_rename_tables_to_english.sql
-- Paste di Supabase SQL Editor → Run
```

### Drop Tabel (Jika Tidak Ada Data):

```sql
-- Copy dari: supabase/migrations/20240101000002_drop_indonesian_tables.sql
-- Paste di Supabase SQL Editor → Run
```

### Create Tabel Baru (Jika Drop):

```sql
-- Copy dari: supabase/migrations/20240101000000_initial_schema.sql
-- Paste di Supabase SQL Editor → Run
```

---

## ✅ Setelah Fix

1. **Verify di Supabase Dashboard:**
   - Table Editor → Pastikan ada tabel dengan nama Inggris
   - `users`, `customers`, `orders`, `billings`, `chat_messages`, `courier_locations`, `payment_proofs`

2. **Deploy Aplikasi:**
   - Aplikasi akan menggunakan tabel dengan nama Inggris
   - Semua fitur akan berfungsi normal

---

## 💡 Tips

- **Backup data dulu** jika tabel Indonesia berisi data penting
- **Test di development** sebelum apply ke production
- **Gunakan auto-create** (Opsi 3) untuk menghindari konflik

---

**Pilih opsi yang sesuai dengan kebutuhan Anda! 🚀**

