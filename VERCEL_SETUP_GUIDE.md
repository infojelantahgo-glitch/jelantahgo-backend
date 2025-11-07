# 🚀 Vercel Setup Guide - Pilih New atau Existing?

## ❓ Pertanyaan: Link to existing project or create new?

### ✅ Jawaban: **NEW** (Create new project)

**Alasan:**
- Ini pertama kali deploy backend ke Vercel
- Akan create project baru
- Lebih mudah untuk setup pertama kali

---

## 📋 Langkah Setelah Pilih "NEW"

### 1. Project Name
**Jawab:** `jelantahgo-backend` (atau nama lain yang Anda mau)

### 2. Directory
**Jawab:** `./` (current directory)

### 3. Override Settings?
**Jawab:** `No` (gunakan default dari vercel.json)

---

## 🔄 Jika Pilih "EXISTING" (Tidak Recommended)

Hanya pilih "existing" jika:
- ✅ Sudah pernah deploy project ini sebelumnya
- ✅ Mau update deployment yang sudah ada
- ✅ Mau deploy ke project yang sama

---

## ✅ Recommended Flow

```
1. vercel login
2. vercel --prod
3. Link to existing project? → NO (pilih NEW)
4. Project name? → jelantahgo-backend
5. Directory? → ./
6. Deploy!
```

---

## 📝 Summary

**Pilih:** **NEW** (Create new project)

**Project Name:** `jelantahgo-backend`

**Directory:** `./`

**Setelah deploy:** Set environment variables di Vercel Dashboard!

---

**🚀 Pilih NEW dan lanjutkan deploy!**

