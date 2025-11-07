# 🚀 Quick Deploy Frontend ke Vercel (CLI)

## ✅ Vercel CLI Sudah Terinstall!

**Version:** `48.8.2`

---

## 🚀 Quick Start

### Step 1: Login ke Vercel

```bash
vercel login
```

Ini akan membuka browser untuk login dengan GitHub.

### Step 2: Deploy Frontend

#### Jika Frontend sudah ada:

```bash
cd jelantahgo-frontend
vercel --prod
```

#### Jika Frontend belum ada, buat dulu:

**React:**
```bash
npx create-react-app jelantahgo-frontend
cd jelantahgo-frontend
vercel --prod
```

**Next.js:**
```bash
npx create-next-app jelantahgo-frontend
cd jelantahgo-frontend
vercel --prod
```

**Vue:**
```bash
npm create vue@latest jelantahgo-frontend
cd jelantahgo-frontend
vercel --prod
```

---

## 🔧 Setup Environment Variables

### Via CLI:

```bash
cd jelantahgo-frontend
vercel env add REACT_APP_API_URL production
```

Input value:
```
https://jelantahgo-backend-production.up.railway.app
```

### Atau buat file `.env.local`:

```env
REACT_APP_API_URL=https://jelantahgo-backend-production.up.railway.app
```

---

## 📋 Complete Workflow

### 1. Login:
```bash
vercel login
```

### 2. Create Frontend (jika belum ada):
```bash
npx create-react-app jelantahgo-frontend
cd jelantahgo-frontend
```

### 3. Setup API Config:
Buat file `.env.local`:
```env
REACT_APP_API_URL=https://jelantahgo-backend-production.up.railway.app
```

### 4. Deploy:
```bash
vercel --prod
```

### 5. Set Environment Variables:
```bash
vercel env add REACT_APP_API_URL production
```

### 6. Link to GitHub (Auto-Deploy):
```bash
vercel link
```

---

## 🎯 Quick Commands

```bash
vercel login              # Login ke Vercel
vercel                    # Deploy preview
vercel --prod            # Deploy production
vercel ls                # List deployments
vercel logs              # View logs
vercel open              # Open in browser
vercel link              # Link to GitHub
vercel env add           # Add environment variable
```

---

## ✅ Checklist

- [x] Vercel CLI installed
- [ ] Logged in to Vercel (`vercel login`)
- [ ] Frontend project created
- [ ] API URL configured
- [ ] Deployed to Vercel (`vercel --prod`)
- [ ] Environment variables set
- [ ] Linked to GitHub (optional)

---

## 🆘 Troubleshooting

### Not logged in:
```bash
vercel login
```

### Deploy failed:
- Cek build command
- Pastikan dependencies terinstall
- Cek logs: `vercel logs`

---

## 📝 Files Created

- ✅ `setup_vercel.bat` - Windows script
- ✅ `setup_vercel.sh` - Linux/Mac script
- ✅ `DEPLOY_VERCEL_CLI.md` - Detailed guide
- ✅ `vercel.json` - Vercel config (optional)

---

**🚀 Ready to deploy! Run `vercel login` lalu `vercel --prod`!**

