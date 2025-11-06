-- ====================================
-- JELANTAHGO DATABASE SCHEMA
-- Initial migration
-- ====================================

-- Customers table (data pelanggan) - HARUS DIBUAT PERTAMA
CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address TEXT NOT NULL,
    referrer_id INTEGER REFERENCES customers(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_customers_email ON customers(email);

-- Users table (admin, customer, courier, warehouse accounts)
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    customer_id INTEGER REFERENCES customers(id)
);

CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_role ON users(role);

-- Orders table (data pesanan pickup)
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    customer_name VARCHAR(100),
    courier_id INTEGER,
    courier_name VARCHAR(100),
    volume_liters FLOAT,
    status VARCHAR(20) DEFAULT 'pending',
    address TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    pickup_date TIMESTAMP,
    completed_at TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_orders_customer ON orders(customer_id);
CREATE INDEX IF NOT EXISTS idx_orders_status ON orders(status);
CREATE INDEX IF NOT EXISTS idx_orders_created ON orders(created_at);

-- Billing table (data tagihan)
CREATE TABLE IF NOT EXISTS billings (
    id SERIAL PRIMARY KEY,
    order_id INTEGER UNIQUE NOT NULL REFERENCES orders(id),
    volume_liters FLOAT NOT NULL,
    base_price_per_liter FLOAT NOT NULL,
    base_total FLOAT NOT NULL,
    courier_fee FLOAT NOT NULL,
    affiliate_fee FLOAT NOT NULL,
    grand_total FLOAT NOT NULL,
    paid BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Chat Messages table (chat customer-courier)
CREATE TABLE IF NOT EXISTS chat_messages (
    id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES orders(id),
    sender_role VARCHAR(20) NOT NULL,
    sender_name VARCHAR(100) NOT NULL,
    message TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_chat_order ON chat_messages(order_id);
CREATE INDEX IF NOT EXISTS idx_chat_timestamp ON chat_messages(timestamp);

-- Courier Locations table (GPS tracking)
CREATE TABLE IF NOT EXISTS courier_locations (
    id SERIAL PRIMARY KEY,
    order_id INTEGER UNIQUE NOT NULL REFERENCES orders(id),
    courier_id INTEGER NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    eta_minutes INTEGER,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Payment Proofs table (bukti pembayaran)
CREATE TABLE IF NOT EXISTS payment_proofs (
    id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES orders(id),
    file_path VARCHAR(500) NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_size INTEGER,
    uploaded_by INTEGER NOT NULL REFERENCES users(id),
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

