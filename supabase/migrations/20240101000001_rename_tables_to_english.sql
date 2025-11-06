-- ====================================
-- RENAME TABLES FROM INDONESIAN TO ENGLISH
-- ====================================
-- 
-- Script ini untuk rename tabel dari bahasa Indonesia ke Inggris
-- sesuai dengan models.py aplikasi
-- ====================================

-- Rename tables dari Indonesia ke Inggris
DO $$ 
BEGIN
    -- Rename pengguna → users (jika ada)
    IF EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'pengguna') THEN
        ALTER TABLE pengguna RENAME TO users;
        RAISE NOTICE 'Table pengguna renamed to users';
    END IF;

    -- Rename pelanggan → customers (jika ada)
    IF EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'pelanggan') THEN
        ALTER TABLE pelanggan RENAME TO customers;
        RAISE NOTICE 'Table pelanggan renamed to customers';
    END IF;

    -- Rename pesanan → orders (jika ada)
    IF EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'pesanan') THEN
        ALTER TABLE pesanan RENAME TO orders;
        RAISE NOTICE 'Table pesanan renamed to orders';
    END IF;

    -- Rename tagihan → billings (jika ada)
    IF EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'tagihan') THEN
        ALTER TABLE tagihan RENAME TO billings;
        RAISE NOTICE 'Table tagihan renamed to billings';
    END IF;

    -- Rename pesan_obrolan → chat_messages (jika ada)
    IF EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'pesan_obrolan') THEN
        ALTER TABLE pesan_obrolan RENAME TO chat_messages;
        RAISE NOTICE 'Table pesan_obrolan renamed to chat_messages';
    END IF;

    -- Rename lokasi_kurir → courier_locations (jika ada)
    IF EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'lokasi_kurir') THEN
        ALTER TABLE lokasi_kurir RENAME TO courier_locations;
        RAISE NOTICE 'Table lokasi_kurir renamed to courier_locations';
    END IF;

    -- Rename bukti_pembayaran → payment_proofs (jika ada)
    IF EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'bukti_pembayaran') THEN
        ALTER TABLE bukti_pembayaran RENAME TO payment_proofs;
        RAISE NOTICE 'Table bukti_pembayaran renamed to payment_proofs';
    END IF;
END $$;

