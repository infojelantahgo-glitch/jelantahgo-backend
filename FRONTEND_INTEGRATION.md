# 🎨 Frontend Integration Guide

## 📋 Status

**Ini adalah BACKEND API STANDALONE** - tidak ada frontend di project ini.

Frontend perlu dibuat terpisah atau mungkin sudah ada di repository lain.

---

## 🔗 Backend API URL

**API Base URL:**
```
https://jelantahgo-backend-production.up.railway.app
```

**API Documentation:**
```
https://jelantahgo-backend-production.up.railway.app/docs
```

---

## 🎨 Frontend Options

### Option 1: Buat Frontend Baru

**Tech Stack yang bisa digunakan:**
- **React** (Recommended)
- **Vue.js**
- **Next.js**
- **Angular**
- **Svelte**

### Option 2: Gunakan Frontend yang Sudah Ada

Jika frontend sudah ada di repository lain, connect ke backend ini dengan:
- **API URL:** `https://jelantahgo-backend-production.up.railway.app`
- **API Docs:** `https://jelantahgo-backend-production.up.railway.app/docs`

---

## 🚀 Quick Start: Setup Frontend

### 1. Buat React App (Contoh)

```bash
npx create-react-app jelantahgo-frontend
cd jelantahgo-frontend
npm install axios
```

### 2. Setup API Configuration

Buat file `src/config/api.js`:

```javascript
const API_BASE_URL = 'https://jelantahgo-backend-production.up.railway.app';

export default API_BASE_URL;
```

### 3. Setup Axios Instance

Buat file `src/api/axios.js`:

```javascript
import axios from 'axios';
import API_BASE_URL from '../config/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests if available
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;
```

### 4. Example: Login Component

```javascript
import React, { useState } from 'react';
import api from '../api/axios';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post('/auth/login', {
        email,
        password,
      });
      
      // Save token
      localStorage.setItem('token', response.data.access_token);
      
      // Redirect to dashboard
      window.location.href = '/dashboard';
    } catch (err) {
      setError('Login failed. Please check your credentials.');
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />
      <button type="submit">Login</button>
      {error && <p>{error}</p>}
    </form>
  );
}

export default Login;
```

### 5. Example: Register Component

```javascript
import React, { useState } from 'react';
import api from '../api/axios';

function Register() {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    name: '',
    phone: '',
    role: 'customer',
  });
  const [error, setError] = useState('');

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      await api.post('/auth/register', formData);
      alert('Registration successful! Please login.');
      window.location.href = '/login';
    } catch (err) {
      setError('Registration failed. Please try again.');
    }
  };

  return (
    <form onSubmit={handleRegister}>
      <input
        type="email"
        value={formData.email}
        onChange={(e) => setFormData({ ...formData, email: e.target.value })}
        placeholder="Email"
      />
      <input
        type="password"
        value={formData.password}
        onChange={(e) => setFormData({ ...formData, password: e.target.value })}
        placeholder="Password"
      />
      <input
        type="text"
        value={formData.name}
        onChange={(e) => setFormData({ ...formData, name: e.target.value })}
        placeholder="Name"
      />
      <input
        type="text"
        value={formData.phone}
        onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
        placeholder="Phone"
      />
      <button type="submit">Register</button>
      {error && <p>{error}</p>}
    </form>
  );
}

export default Register;
```

---

## 🔐 Authentication Flow

### 1. Login

```javascript
POST /auth/login
Body: {
  "email": "user@example.com",
  "password": "password123"
}

Response: {
  "access_token": "eyJhbGc...",
  "token_type": "bearer"
}
```

### 2. Save Token

```javascript
localStorage.setItem('token', response.data.access_token);
```

### 3. Use Token in Requests

```javascript
headers: {
  'Authorization': `Bearer ${token}`
}
```

### 4. Get Current User

```javascript
GET /auth/me
Headers: {
  'Authorization': 'Bearer <token>'
}
```

---

## 📡 API Endpoints untuk Frontend

### Authentication
- `POST /auth/register` - Register user
- `POST /auth/login` - Login
- `GET /auth/me` - Get current user

### Dashboard
- `POST /dashboard` - Get dashboard data

### Customer
- `POST /customer/register` - Register customer
- `GET /customer/{customer_id}` - Get customer

### Orders
- `POST /order/create` - Create order
- `POST /order/list` - List orders
- `GET /order/{order_id}` - Get order

### Location Tracking
- `POST /location/update` - Update location
- `POST /location/get` - Get location

### Chat
- `POST /chat/send` - Send message
- `POST /chat/get` - Get chat history

### Payment Proof
- `POST /payment-proof/upload` - Upload proof
- `GET /payment-proof/{order_id}` - Get proof

---

## 🌐 CORS Configuration

Backend sudah dikonfigurasi untuk allow semua origins:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Frontend bisa langsung connect tanpa masalah CORS.

---

## 🚀 Deploy Frontend

### Option 1: Vercel (Recommended untuk React/Next.js)

1. **Push code ke GitHub**
2. **Buka [vercel.com](https://vercel.com)**
3. **Import project dari GitHub**
4. **Deploy**

### Option 2: Netlify

1. **Push code ke GitHub**
2. **Buka [netlify.com](https://netlify.com)**
3. **New site from Git**
4. **Deploy**

### Option 3: Railway (Same as Backend)

1. **Push code ke GitHub**
2. **Railway Dashboard → New → GitHub Repo**
3. **Deploy**

---

## 📚 API Documentation

**Full API Documentation:**
```
https://jelantahgo-backend-production.up.railway.app/docs
```

**ReDoc (Alternative):**
```
https://jelantahgo-backend-production.up.railway.app/redoc
```

---

## ✅ Checklist Frontend Integration

- [ ] Buat frontend project (React/Vue/Next.js)
- [ ] Setup API configuration (base URL)
- [ ] Setup axios/fetch untuk API calls
- [ ] Implement authentication (login/register)
- [ ] Implement protected routes
- [ ] Connect ke backend API
- [ ] Test semua endpoints
- [ ] Deploy frontend

---

## 🆘 Troubleshooting

### CORS Error

**Problem:** CORS error saat connect dari frontend

**Solution:** Backend sudah dikonfigurasi untuk allow semua origins. Pastikan frontend menggunakan HTTPS.

### Authentication Error

**Problem:** 401 Unauthorized

**Solution:** 
- Pastikan token disimpan setelah login
- Pastikan token dikirim di header: `Authorization: Bearer <token>`
- Cek apakah token expired

### API Connection Error

**Problem:** Cannot connect to API

**Solution:**
- Cek API URL: `https://jelantahgo-backend-production.up.railway.app`
- Test di browser: `https://jelantahgo-backend-production.up.railway.app/health`
- Cek CORS configuration

---

## 📝 Summary

**Backend Status:** ✅ **READY**

- ✅ API running di Railway
- ✅ Database connected
- ✅ All endpoints working
- ✅ CORS configured
- ✅ Authentication ready

**Frontend:** ⚠️ **Perlu dibuat atau connect ke yang sudah ada**

---

**Backend API siap digunakan oleh frontend! 🚀**

Hubungkan frontend ke: `https://jelantahgo-backend-production.up.railway.app`

