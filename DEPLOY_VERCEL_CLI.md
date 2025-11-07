# 🚀 Deploy Frontend ke Vercel menggunakan CLI

## 📋 Prerequisites

1. **Node.js & npm** sudah terinstall
2. **Vercel CLI** sudah terinstall (akan di-install)
3. **Frontend code** sudah siap

---

## 🔧 Step 1: Install Vercel CLI

```bash
npm install -g vercel
```

Atau jika menggunakan npx (tidak perlu install global):
```bash
npx vercel
```

---

## 🔐 Step 2: Login ke Vercel

```bash
vercel login
```

Ini akan:
1. Buka browser untuk login
2. Login dengan GitHub (recommended)
3. Authorize Vercel

---

## 📁 Step 3: Setup Frontend Project

### Jika Frontend belum ada, buat dulu:

#### Option A: React App

```bash
npx create-react-app jelantahgo-frontend
cd jelantahgo-frontend
```

#### Option B: Next.js App

```bash
npx create-next-app jelantahgo-frontend
cd jelantahgo-frontend
```

#### Option C: Vue App

```bash
npm create vue@latest jelantahgo-frontend
cd jelantahgo-frontend
```

---

## 🌐 Step 4: Setup API Configuration

Buat file `.env.local` (untuk local development):

```env
REACT_APP_API_URL=https://jelantahgo-backend-production.up.railway.app
```

Atau untuk Next.js:
```env
NEXT_PUBLIC_API_URL=https://jelantahgo-backend-production.up.railway.app
```

Atau untuk Vue:
```env
VUE_APP_API_URL=https://jelantahgo-backend-production.up.railway.app
```

---

## 🚀 Step 5: Deploy ke Vercel

### Deploy untuk pertama kali:

```bash
cd jelantahgo-frontend
vercel
```

Ini akan:
1. Ask beberapa pertanyaan:
   - **Set up and deploy?** → Yes
   - **Which scope?** → Pilih account
   - **Link to existing project?** → No (untuk pertama kali)
   - **What's your project's name?** → `jelantahgo-frontend`
   - **In which directory is your code located?** → `./`
2. Deploy project
3. Give you URL: `https://jelantahgo-frontend.vercel.app`

### Deploy ke production:

```bash
vercel --prod
```

Ini akan deploy ke production domain.

---

## 🔄 Step 6: Link ke GitHub (Auto-Deploy)

### Link project ke GitHub repository:

```bash
vercel link
```

Ini akan:
1. Ask untuk link existing project atau create new
2. Link ke GitHub repository
3. Setup auto-deploy

### Atau setup di Vercel Dashboard:

1. Buka https://vercel.com/dashboard
2. Pilih project
3. Settings → Git
4. Connect repository

---

## 🌍 Step 7: Set Environment Variables

### Via CLI:

```bash
vercel env add REACT_APP_API_URL production
```

Input value:
```
https://jelantahgo-backend-production.up.railway.app
```

### Via Dashboard:

1. Buka https://vercel.com/dashboard
2. Pilih project
3. Settings → Environment Variables
4. Add variable:
   - **Key:** `REACT_APP_API_URL`
   - **Value:** `https://jelantahgo-backend-production.up.railway.app`
   - **Environment:** Production, Preview, Development

---

## 📝 Step 8: Create vercel.json (Optional)

Buat file `vercel.json` di root project:

```json
{
  "version": 2,
  "buildCommand": "npm run build",
  "outputDirectory": "build",
  "framework": "create-react-app",
  "env": {
    "REACT_APP_API_URL": "https://jelantahgo-backend-production.up.railway.app"
  }
}
```

Atau untuk Next.js (tidak perlu vercel.json, auto-detect):
```json
{
  "version": 2,
  "framework": "nextjs"
}
```

---

## 🔄 Step 9: Auto-Deploy dari GitHub

### Setup GitHub Integration:

1. **Push code ke GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/jelantahgo-frontend.git
   git push -u origin main
   ```

2. **Link di Vercel:**
   ```bash
   vercel link
   ```

3. **Setiap push ke GitHub akan auto-deploy!** ✅

---

## 📋 Quick Commands

### Deploy:
```bash
vercel                    # Deploy to preview
vercel --prod            # Deploy to production
```

### List deployments:
```bash
vercel ls
```

### View logs:
```bash
vercel logs
```

### Open project in browser:
```bash
vercel open
```

### Remove deployment:
```bash
vercel remove
```

---

## 🎯 Complete Workflow

### 1. Setup Project:
```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy
cd jelantahgo-frontend
vercel
```

### 2. Link to GitHub:
```bash
vercel link
```

### 3. Set Environment Variables:
```bash
vercel env add REACT_APP_API_URL production
```

### 4. Deploy to Production:
```bash
vercel --prod
```

### 5. Auto-Deploy Setup:
- Push code ke GitHub
- Vercel akan auto-deploy setiap push!

---

## ✅ Checklist

- [ ] Vercel CLI installed
- [ ] Logged in to Vercel
- [ ] Frontend project created
- [ ] API URL configured
- [ ] Deployed to Vercel
- [ ] Environment variables set
- [ ] Linked to GitHub
- [ ] Auto-deploy enabled

---

## 🆘 Troubleshooting

### Error: Not logged in

```bash
vercel login
```

### Error: Project not found

```bash
vercel link
```

### Error: Build failed

- Cek build command di `package.json`
- Pastikan dependencies terinstall
- Cek logs: `vercel logs`

### Error: Environment variable not working

- Pastikan variable name benar (REACT_APP_* untuk React)
- Redeploy setelah set variable: `vercel --prod`

---

## 📝 Summary

**Quick Deploy:**
```bash
npm install -g vercel
vercel login
cd jelantahgo-frontend
vercel --prod
```

**Backend API URL:**
```
https://jelantahgo-backend-production.up.railway.app
```

---

**🚀 Deploy frontend ke Vercel menggunakan CLI sekarang!**

