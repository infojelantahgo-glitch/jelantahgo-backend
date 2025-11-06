# 🔧 Install Supabase CLI di Windows

## ⚠️ Catatan Penting

Supabase CLI **tidak bisa diinstall via `npm install -g`** di Windows. Perlu pakai metode alternatif.

---

## ✅ Metode 1: Download Binary (Paling Mudah)

### Step 1: Download Binary

1. **Buka:** https://github.com/supabase/cli/releases
2. **Download:** `supabase_windows_amd64.zip` (atau sesuai arsitektur Anda)
3. **Extract** zip file
4. **Rename** `supabase.exe` (jika perlu)

### Step 2: Add ke PATH

1. **Copy `supabase.exe`** ke folder yang ada di PATH, misalnya:
   - `C:\Windows\System32\`
   - Atau buat folder baru: `C:\supabase\`
   - Tambahkan folder ke PATH environment variable

2. **Atau buat folder dan add ke PATH:**
   ```powershell
   # Buat folder
   mkdir C:\supabase
   
   # Copy supabase.exe ke folder tersebut
   # (extract dari zip yang sudah di-download)
   
   # Add ke PATH (perlu admin)
   [Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\supabase", "User")
   ```

### Step 3: Verify

```bash
supabase --version
```

---

## ✅ Metode 2: Pakai Scoop (Jika Sudah Install)

### Install Scoop (jika belum):

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
```

### Install Supabase CLI:

```bash
scoop bucket add supabase https://github.com/supabase/scoop-bucket.git
scoop install supabase
```

### Verify:

```bash
supabase --version
```

---

## ✅ Metode 3: Pakai npx (Tanpa Install Global)

Bisa pakai Supabase CLI langsung tanpa install:

```bash
npx supabase login
npx supabase link --project-ref ybzzfgzzfrozxrujmjeo
npx supabase db push
```

**Note:** Perlu internet connection setiap kali run.

---

## 🚀 Quick Start Setelah Install

### 1. Login

```bash
supabase login
# Atau jika pakai npx:
npx supabase login
```

### 2. Link Project

```bash
supabase link --project-ref ybzzfgzzfrozxrujmjeo
# Atau:
npx supabase link --project-ref ybzzfgzzfrozxrujmjeo
```

**Atau dengan connection string:**
```bash
supabase link --db-url postgresql://postgres:jelantahgo-db@db.ybzzfgzzfrozxrujmjeo.supabase.co:5432/postgres
```

### 3. Run Migration

```bash
supabase db push
# Atau:
npx supabase db push
```

---

## 💡 Rekomendasi

**Untuk Windows, gunakan `npx` (Metode 3)** karena:
- ✅ Tidak perlu install
- ✅ Tidak perlu setup PATH
- ✅ Langsung bisa digunakan
- ⚠️ Perlu internet setiap kali run

**Atau download binary** (Metode 1) jika ingin install permanen.

---

## 🔗 Links

- **Releases:** https://github.com/supabase/cli/releases
- **Docs:** https://supabase.com/docs/reference/cli

---

## ✅ Checklist

- [ ] Download binary atau install via Scoop atau pakai npx
- [ ] Verify: `supabase --version` atau `npx supabase --version`
- [ ] Login: `supabase login` atau `npx supabase login`
- [ ] Link project: `supabase link --project-ref ybzzfgzzfrozxrujmjeo`
- [ ] Run migration: `supabase db push`

---

**Selamat mencoba! 🚀**

