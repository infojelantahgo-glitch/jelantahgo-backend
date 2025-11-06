# 🔐 Cara Push ke GitHub Repository

## ❌ Error yang Terjadi

```
Permission denied to infojelantahgo-glitch/jelantahgo-backend.git
```

## ✅ Solusi

### Opsi 1: Login dengan Akun yang Punya Akses (Paling Mudah)

1. **Pastikan Anda login dengan akun yang punya akses ke repository:**
   - Akun: `infojelantahgo-glitch` (atau akun yang di-invite)
   
2. **Atau minta owner repository untuk:**
   - Invite Anda sebagai collaborator
   - Settings → Collaborators → Add people
   - Masukkan username GitHub Anda

3. **Jika sudah punya akses, push dengan:**
   ```bash
   git push -u origin main
   ```
   (Anda akan diminta login jika belum)

---

### Opsi 2: Gunakan Personal Access Token (Recommended)

1. **Buat Personal Access Token:**
   - Buka: https://github.com/settings/tokens
   - Klik **"Generate new token"** → **"Generate new token (classic)"**
   - **Note:** `jelantahgo-backend-push`
   - **Expiration:** Sesuaikan (90 days atau custom)
   - **Scopes:** Centang **`repo`** (full control)
   - Klik **"Generate token"**
   - **PENTING:** Copy token sekarang (tidak bisa dilihat lagi nanti!)

2. **Push dengan token:**
   ```bash
   git push https://YOUR_TOKEN@github.com/infojelantahgo-glitch/jelantahgo-backend.git main
   ```
   
   Ganti `YOUR_TOKEN` dengan token yang sudah di-copy.

3. **Atau simpan credential (agar tidak perlu input setiap kali):**
   ```bash
   git remote set-url origin https://YOUR_TOKEN@github.com/infojelantahgo-glitch/jelantahgo-backend.git
   git push -u origin main
   ```

---

### Opsi 3: Fork Repository (Jika Tidak Punya Akses)

1. **Fork repository:**
   - Buka: https://github.com/infojelantahgo-glitch/jelantahgo-backend
   - Klik **"Fork"** (pojok kanan atas)
   - Pilih akun Anda sebagai destination

2. **Push ke fork Anda:**
   ```bash
   git remote remove origin
   git remote add origin https://github.com/YOUR_USERNAME/jelantahgo-backend.git
   git push -u origin main
   ```

3. **Buat Pull Request:**
   - Buka repository fork Anda di GitHub
   - Klik **"Contribute"** → **"Open pull request"**
   - Pilih base: `infojelantahgo-glitch/jelantahgo-backend` ← `YOUR_USERNAME/jelantahgo-backend`

---

## 🔑 Cara Login Git dengan Token

### Windows (Git Credential Manager)

1. **Saat push, akan muncul popup login:**
   - **Username:** Username GitHub Anda
   - **Password:** Masukkan Personal Access Token (bukan password!)

2. **Atau setup credential helper:**
   ```bash
   git config --global credential.helper manager-core
   ```

### Linux/Mac

1. **Setup credential helper:**
   ```bash
   git config --global credential.helper store
   ```

2. **Push akan meminta credential sekali, lalu tersimpan**

---

## 📋 Quick Command Reference

```bash
# Cek remote
git remote -v

# Set remote dengan token
git remote set-url origin https://TOKEN@github.com/infojelantahgo-glitch/jelantahgo-backend.git

# Push
git push -u origin main

# Cek status
git status
```

---

## ✅ Setelah Berhasil Push

1. **Cek repository di GitHub:**
   https://github.com/infojelantahgo-glitch/jelantahgo-backend

2. **Pastikan semua file sudah ada:**
   - ✅ main.py
   - ✅ requirements.txt
   - ✅ render.yaml
   - ✅ DEPLOY_INSTRUCTIONS.md
   - ✅ dll

3. **Lanjut deploy ke Render:**
   - Ikuti panduan di `DEPLOY_INSTRUCTIONS.md`

---

## 🆘 Masih Error?

Jika masih ada masalah:

1. **Cek permission repository:**
   - Apakah Anda punya akses write?
   - Apakah repository private/public?

2. **Cek git credential:**
   ```bash
   git config --global --list
   ```

3. **Clear credential cache:**
   ```bash
   git credential-manager-core erase
   ```

4. **Coba dengan SSH (jika sudah setup SSH key):**
   ```bash
   git remote set-url origin git@github.com:infojelantahgo-glitch/jelantahgo-backend.git
   git push -u origin main
   ```

---

**Selamat mencoba! 🚀**

