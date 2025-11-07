# 🌐 Vercel Deployment URL

## 🔍 Cara Cek URL Deployment

### Method 1: Dari Terminal (Setelah Deploy)

Setelah `vercel --prod`, URL akan muncul di output:

```
✅ Production: https://jelantahgo-backend-[hash].vercel.app
```

### Method 2: Vercel Dashboard

1. **Buka:** https://vercel.com/dashboard
2. **Pilih project:** `jelantahgo-backend`
3. **Tab "Deployments"**
4. **Klik deployment terbaru**
5. **URL ada di bagian atas:** `https://jelantahgo-backend-[hash].vercel.app`

### Method 3: Via CLI

```bash
vercel ls
```

Ini akan menampilkan semua deployments dan URL-nya.

---

## 📋 Format URL Vercel

**Production URL:**
```
https://jelantahgo-backend-[hash].vercel.app
```

**Preview URL (setiap commit):**
```
https://jelantahgo-backend-git-[branch]-[username].vercel.app
```

**Custom Domain (jika setup):**
```
https://your-custom-domain.com
```

---

## 🔗 Quick Links

### Setelah Deploy, URL biasanya:
- **Production:** `https://jelantahgo-backend-[hash].vercel.app`
- **Preview:** `https://jelantahgo-backend-git-main-[username].vercel.app`

### Cek di Vercel Dashboard:
- **Dashboard:** https://vercel.com/dashboard
- **Project:** https://vercel.com/dashboard/[project-name]

---

## 🧪 Test URL

Setelah dapat URL, test:

### Health Check:
```
https://your-app.vercel.app/health
```

Expected:
```json
{
  "status": "healthy",
  "service": "JelantahGO Backend"
}
```

### API Docs:
```
https://your-app.vercel.app/docs
```

---

## ✅ Summary

**URL akan muncul:**
1. ✅ Di terminal setelah deploy
2. ✅ Di Vercel Dashboard
3. ✅ Via `vercel ls` command

**Format:** `https://jelantahgo-backend-[hash].vercel.app`

---

**Cek Vercel Dashboard atau jalankan `vercel ls` untuk lihat URL!**

