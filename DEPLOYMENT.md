# 🚀 Deployment Guide - JelantahGO Backend

Panduan lengkap untuk deploy aplikasi JelantahGO Backend ke berbagai platform.

## 📋 Daftar Isi

1. [GitHub Actions (CI/CD)](#github-actions-cicd)
2. [Railway](#railway)
3. [Render](#render)
4. [VPS (Ubuntu/Debian)](#vps-ubuntudebian)
5. [Docker](#docker)
6. [Environment Variables](#environment-variables)

---

## 🔄 GitHub Actions (CI/CD)

GitHub Actions sudah dikonfigurasi untuk:
- ✅ Run tests saat push
- ✅ Check code syntax
- ✅ Auto deploy ke production

### Setup GitHub Actions

1. **Push code ke GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/username/jelantahgo-backend.git
   git push -u origin main
   ```

2. **Setup Secrets (jika deploy ke VPS):**
   - Go to: Repository → Settings → Secrets and variables → Actions
   - Add secrets:
     - `VPS_HOST`: IP atau domain VPS
     - `VPS_USER`: Username SSH
     - `VPS_SSH_KEY`: Private SSH key

3. **Workflow akan otomatis jalan saat push ke `main` branch**

---

## 🚂 Railway

Railway adalah platform cloud yang mudah digunakan dengan auto-deploy dari GitHub.

### Setup Railway

1. **Buat akun di [railway.app](https://railway.app)**

2. **Create New Project:**
   - Klik "New Project"
   - Pilih "Deploy from GitHub repo"
   - Pilih repository Anda

3. **Setup Database:**
   - Klik "New" → "Database" → "Add PostgreSQL"
   - Railway akan otomatis membuat database

4. **Setup Environment Variables:**
   - Go to project settings → Variables
   - Add variables:
     ```
     DATABASE_URL=<railway-provided-url>
     JWT_SECRET=<generate-strong-secret>
     SMTP_HOST=smtp.gmail.com
     SMTP_PORT=587
     SMTP_USER=your-email@gmail.com
     SMTP_PASSWORD=your-app-password
     EMAIL_FROM=your-email@gmail.com
     ```

5. **Deploy:**
   - Railway akan otomatis deploy saat push ke GitHub
   - Atau klik "Deploy" manual

### Railway Auto-Deploy

Railway akan otomatis:
- ✅ Detect Python project
- ✅ Install dependencies dari `requirements.txt`
- ✅ Run `python main.py`
- ✅ Auto-restart saat ada update

---

## 🎨 Render

Render adalah alternatif platform cloud dengan free tier.

### Setup Render

1. **Buat akun di [render.com](https://render.com)**

2. **Create New Web Service:**
   - Klik "New" → "Web Service"
   - Connect GitHub repository
   - Settings:
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `python main.py`
     - **Environment:** Python 3

3. **Setup PostgreSQL Database:**
   - Klik "New" → "PostgreSQL"
   - Render akan otomatis membuat database
   - Copy connection string

4. **Setup Environment Variables:**
   - Go to Environment tab
   - Add variables:
     ```
     DATABASE_URL=<render-postgres-url>
     JWT_SECRET=<generate-strong-secret>
     API_HOST=0.0.0.0
     API_PORT=10000
     SMTP_HOST=smtp.gmail.com
     SMTP_PORT=587
     SMTP_USER=your-email@gmail.com
     SMTP_PASSWORD=your-app-password
     EMAIL_FROM=your-email@gmail.com
     ```

5. **Deploy:**
   - Render akan otomatis deploy saat push
   - Atau klik "Manual Deploy"

---

## 🖥️ VPS (Ubuntu/Debian)

Deploy ke VPS sendiri dengan full control.

### Prerequisites

- VPS dengan Ubuntu 20.04+ atau Debian 11+
- SSH access
- Domain (optional, untuk SSL)

### Setup VPS

1. **SSH ke VPS:**
   ```bash
   ssh user@your-vps-ip
   ```

2. **Install Dependencies:**
   ```bash
   # Update system
   sudo apt update && sudo apt upgrade -y
   
   # Install Python
   sudo apt install python3 python3-pip python3-venv -y
   
   # Install PostgreSQL
   sudo apt install postgresql postgresql-contrib -y
   
   # Install Nginx (reverse proxy)
   sudo apt install nginx -y
   
   # Install Git
   sudo apt install git -y
   ```

3. **Setup PostgreSQL:**
   ```bash
   sudo -u postgres psql
   ```
   ```sql
   CREATE DATABASE jelantahgo_db;
   CREATE USER jelantahgo WITH PASSWORD 'your-strong-password';
   GRANT ALL PRIVILEGES ON DATABASE jelantahgo_db TO jelantahgo;
   \q
   ```

4. **Clone Repository:**
   ```bash
   cd /var/www
   sudo git clone https://github.com/username/jelantahgo-backend.git
   cd jelantahgo-backend
   sudo chown -R $USER:$USER .
   ```

5. **Setup Application:**
   ```bash
   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Create .env file
   cp .env.example .env
   nano .env  # Edit dengan konfigurasi VPS
   ```

6. **Setup Systemd Service:**
   ```bash
   sudo nano /etc/systemd/system/jelantahgo-backend.service
   ```
   ```ini
   [Unit]
   Description=JelantahGO Backend API
   After=network.target

   [Service]
   User=www-data
   WorkingDirectory=/var/www/jelantahgo-backend
   Environment="PATH=/var/www/jelantahgo-backend/venv/bin"
   ExecStart=/var/www/jelantahgo-backend/venv/bin/python main.py
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable jelantahgo-backend
   sudo systemctl start jelantahgo-backend
   ```

7. **Setup Nginx:**
   ```bash
   sudo nano /etc/nginx/sites-available/jelantahgo-backend
   ```
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```
   ```bash
   sudo ln -s /etc/nginx/sites-available/jelantahgo-backend /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   ```

8. **Setup SSL (Let's Encrypt):**
   ```bash
   sudo apt install certbot python3-certbot-nginx -y
   sudo certbot --nginx -d yourdomain.com
   ```

### Auto-Deploy dengan GitHub Webhook

1. **Install webhook receiver:**
   ```bash
   pip install flask
   ```

2. **Create webhook script** (atau gunakan GitHub Actions dengan SSH)

3. **Setup deploy script:**
   ```bash
   chmod +x deploy.sh
   ```

---

## 🐳 Docker

Deploy menggunakan Docker untuk isolasi dan portability.

### Create Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
```

### Build & Run

```bash
# Build image
docker build -t jelantahgo-backend .

# Run container
docker run -d \
  --name jelantahgo-backend \
  -p 8000:8000 \
  --env-file .env \
  jelantahgo-backend
```

### Docker Compose

```yaml
version: '3.8'

services:
  backend:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db

  db:
    image: postgres:14
    environment:
      POSTGRES_DB: jelantahgo_db
      POSTGRES_USER: jelantahgo
      POSTGRES_PASSWORD: jelantahgo123
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

---

## 🔐 Environment Variables

Pastikan semua environment variables di-set dengan benar:

### Required Variables

```env
DATABASE_URL=postgresql://user:password@host:port/database
JWT_SECRET=your-very-strong-secret-key-here
```

### Optional Variables

```env
API_HOST=0.0.0.0
API_PORT=8000
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
EMAIL_FROM=your-email@gmail.com
```

### Generate Strong JWT Secret

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

---

## ✅ Post-Deployment Checklist

- [ ] Database connected dan tables created
- [ ] Environment variables configured
- [ ] Health check endpoint working: `/health`
- [ ] API documentation accessible: `/docs`
- [ ] SSL certificate installed (production)
- [ ] Backup strategy configured
- [ ] Monitoring setup (optional)
- [ ] Log rotation configured

---

## 🆘 Troubleshooting

### Application tidak start
- Cek logs: `journalctl -u jelantahgo-backend -f`
- Cek database connection
- Cek environment variables

### Database connection error
- Verify DATABASE_URL format
- Check PostgreSQL is running
- Verify credentials

### Port already in use
- Change API_PORT in .env
- Kill process using port: `lsof -ti:8000 | xargs kill`

---

## 📚 Resources

- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [Railway Docs](https://docs.railway.app/)
- [Render Docs](https://render.com/docs)
- [Nginx Reverse Proxy](https://nginx.org/en/docs/http/ngx_http_proxy_module.html)

---

**Selamat deploy! 🚀**

