# JelantahGO Backend - Standalone Version

Backend API standalone untuk sistem manajemen pickup minyak jelantah menggunakan **FastAPI + PostgreSQL**.

## 🎯 Fitur Utama

- ✅ Multi-role dashboard (Admin, Customer, Courier, Warehouse)
- ✅ Manajemen customer dengan referral tracking
- ✅ Sistem order pickup lengkap
- ✅ Real-time GPS tracking kurir
- ✅ Live chat customer-courier
- ✅ Perhitungan billing otomatis (tiered pricing)
- ✅ Komisi kurir & affiliate
- ✅ RESTful API dengan dokumentasi otomatis (Swagger)

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Server**: Uvicorn

---

## 📋 Prerequisites

Pastikan sudah terinstall:

1. **Python 3.11+**
2. **PostgreSQL 14+**
3. **pip** (Python package manager)

---

## 🚀 Setup & Installation

### 1. Install PostgreSQL

**macOS (via Homebrew):**
```bash
brew install postgresql@14
brew services start postgresql@14
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
```

**Windows:**
Download installer dari [postgresql.org](https://www.postgresql.org/download/windows/)

### 2. Buat Database

Login ke PostgreSQL:
```bash
psql -U postgres
```

Buat database dan user:
```sql
CREATE DATABASE jelantahgo_db;
CREATE USER jelantahgo WITH PASSWORD 'jelantahgo123';
GRANT ALL PRIVILEGES ON DATABASE jelantahgo_db TO jelantahgo;
\q
```

### 3. Setup Python Environment

```bash
# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Konfigurasi Environment Variables

Copy `.env.example` menjadi `.env`:
```bash
cp .env.example .env
```

Edit `.env` sesuai kebutuhan:
```env
DATABASE_URL=postgresql://jelantahgo:jelantahgo123@localhost/jelantahgo_db
API_HOST=0.0.0.0
API_PORT=8000

# JWT Secret (untuk authentication)
JWT_SECRET=your-secret-key-change-in-production

# Email Configuration (untuk notifications)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
EMAIL_FROM=your-email@gmail.com
```

### 5. Jalankan Server

```bash
python main.py
```

Server akan berjalan di: **http://localhost:8000**

---

## 📚 API Documentation

Setelah server berjalan, buka browser:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 🔗 API Endpoints

### Authentication
- `POST /auth/register` - Register user baru (admin, customer, courier, warehouse)
- `POST /auth/login` - Login dan dapatkan JWT token
- `GET /auth/me` - Get info user yang sedang login (requires authentication)

### Dashboard
- `POST /` - Get role-specific dashboard

### Customer Management
- `POST /customer/register` - Register customer baru
- `GET /customer/{customer_id}` - Get customer by ID

### Order Management
- `POST /order/create` - Buat order pickup baru (sends email confirmation)
- `POST /order/assign` - Assign courier ke order (Admin only, requires auth, sends email)
- `POST /order/update-status` - Update status order (sends email when completed)
- `POST /order/list` - List orders berdasarkan role
- `GET /order/{order_id}` - Get order by ID

### Location Tracking
- `POST /location/update` - Update lokasi kurir real-time
- `POST /location/get` - Get lokasi kurir untuk order

### Chat
- `POST /chat/send` - Kirim chat message
- `POST /chat/get` - Get chat history

### Billing
- `POST /billing/calculate` - Hitung billing order

### File Upload
- `POST /payment-proof/upload` - Upload bukti pembayaran (Admin only, requires auth, sends email)
- `GET /payment-proof/{order_id}` - Get bukti pembayaran untuk order (requires auth)

### Health Check
- `GET /health` - Check server status

---

## 💰 Pricing & Commissions

### Tiered Pricing
- **1-99L**: Rp6,500/liter
- **100-200L**: Rp7,000/liter
- **201+L**: Rp7,500/liter

### Commissions
- **Courier fee**: Rp1,000/liter
- **Affiliate fee**: Rp200/liter (jika ada referrer)

---

## 📁 Project Structure

```
jelantahgo_backend_standalone/
├── main.py              # FastAPI application
├── models.py            # SQLAlchemy database models
├── schemas.py           # Pydantic validation schemas
├── database.py          # Database connection & config
├── crud.py              # Database operations
├── auth.py              # JWT authentication & authorization
├── email_service.py     # Email notification service
├── file_upload.py       # File upload handling
├── init_db.py           # Database initialization script
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
├── uploads/             # Uploaded files directory
│   └── payment_proofs/  # Payment proof files
└── README.md            # Documentation (this file)
```

---

## 🧪 Testing API

### Menggunakan Swagger UI

1. Buka http://localhost:8000/docs
2. Klik endpoint yang ingin di-test
3. Klik "Try it out"
4. Isi request body
5. Klik "Execute"

### Menggunakan curl

**Register Customer:**
```bash
curl -X POST "http://localhost:8000/customer/register" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Budi Santoso",
    "email": "budi@example.com",
    "phone": "+628123456789",
    "address": "Jl. Sudirman No. 123, Jakarta"
  }'
```

**Login:**
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@example.com",
    "password": "password123"
  }'
```

**Create Order:**
```bash
curl -X POST "http://localhost:8000/order/create" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": 1,
    "address": "Jl. Gatot Subroto No. 45"
  }'
```

**Upload Payment Proof (Admin):**
```bash
curl -X POST "http://localhost:8000/payment-proof/upload?order_id=1" \
  -H "Authorization: Bearer <your-token>" \
  -F "file=@/path/to/proof.jpg"
```

---

## 🔧 Development

### Menambah Fitur Baru

1. Tambahkan model di `models.py`
2. Buat schema di `schemas.py`
3. Implementasi CRUD di `crud.py`
4. Tambahkan endpoint di `main.py`

### Database Migration (Opsional)

Jika ingin menggunakan Alembic untuk migration:

```bash
pip install alembic
alembic init alembic
# Edit alembic.ini dan alembic/env.py
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

---

## 🐛 Troubleshooting

### Database Connection Error

```
sqlalchemy.exc.OperationalError: could not connect to server
```

**Solusi:**
- Pastikan PostgreSQL sudah berjalan: `sudo systemctl status postgresql`
- Cek kredensial di `.env`
- Pastikan database sudah dibuat

### Port Already in Use

```
ERROR: [Errno 48] Address already in use
```

**Solusi:**
- Ubah port di `.env`: `API_PORT=8001`
- Atau matikan aplikasi yang menggunakan port 8000

---

## 📦 Production Deployment

### Menggunakan Gunicorn

```bash
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000
```

### Menggunakan Nginx (Reverse Proxy)

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## 🔐 Security Recommendations

1. **Ganti database password** di production
2. **✅ Authentication** (JWT tokens) - Sudah diimplementasikan
3. **Enable HTTPS** dengan SSL certificate
4. **Rate limiting** untuk API endpoints
5. **Input validation** sudah termasuk via Pydantic
6. **Ganti JWT_SECRET** di production dengan secret key yang kuat
7. **Gunakan App Password** untuk Gmail SMTP (jika menggunakan Gmail)

---

## 📞 Support

Jika ada pertanyaan atau masalah:

1. Cek dokumentasi API di `/docs`
2. Review kode di file-file terkait
3. Pastikan database sudah setup dengan benar

---

## 📝 License

Free to use for JelantahGO project.

---

## 🎓 Next Steps

1. **✅ Authentication** (JWT) - Sudah diimplementasikan
2. **✅ Email notifications** - Sudah diimplementasikan
3. **✅ File upload** untuk bukti pickup - Sudah diimplementasikan
4. ~~**Integrasi payment gateway**~~ - Tidak diperlukan (bukti bayar diupload admin)
5. **Deploy ke VPS** atau cloud
6. **Tambahkan unit tests**
7. **Implementasi warehouse role** functionality

## 🔑 Authentication

API menggunakan JWT (JSON Web Tokens) untuk authentication. Setelah login, gunakan token di header:

```
Authorization: Bearer <your-token>
```

### Role-based Access Control:
- **admin**: Akses penuh, bisa upload payment proof, assign courier
- **customer**: Akses terbatas ke order mereka sendiri
- **courier**: Akses ke order yang ditugaskan
- **warehouse**: (Coming soon)

## 📧 Email Notifications

Sistem mengirim email otomatis untuk:
- ✅ Konfirmasi order baru
- ✅ Notifikasi kurir ditugaskan
- ✅ Notifikasi order selesai
- ✅ Notifikasi bukti pembayaran tersedia

**Note**: Email hanya akan dikirim jika SMTP dikonfigurasi di `.env`. Jika tidak dikonfigurasi, sistem akan tetap berjalan tetapi tidak mengirim email.

## 📎 File Upload

Admin dapat mengupload bukti pembayaran melalui endpoint `/payment-proof/upload`. File yang diupload akan:
- Disimpan di folder `uploads/payment_proofs/`
- Dapat diakses melalui URL `/files/payment_proofs/{filename}`
- Otomatis mengupdate status billing menjadi "paid"
- Mengirim email notifikasi ke customer

**Supported file types**: JPG, JPEG, PNG, PDF
**Maximum file size**: 10 MB

Selamat coding! 🚀
