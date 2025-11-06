-- Script untuk setup database JelantahGO
-- Jalankan dengan: psql -U postgres -f setup_database.sql
-- Atau copy-paste ke psql prompt

-- Buat database
CREATE DATABASE jelantahgo_db;

-- Buat user
CREATE USER jelantahgo WITH PASSWORD 'jelantahgo123';

-- Berikan privileges
GRANT ALL PRIVILEGES ON DATABASE jelantahgo_db TO jelantahgo;

-- Connect ke database dan berikan schema privileges
\c jelantahgo_db
GRANT ALL ON SCHEMA public TO jelantahgo;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO jelantahgo;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO jelantahgo;

