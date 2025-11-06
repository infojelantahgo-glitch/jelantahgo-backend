-- ====================================
-- DROP INDONESIAN TABLES (Jika Ada)
-- ====================================
-- 
-- Script ini untuk DROP tabel Indonesia jika sudah ada tabel Inggris
-- HATI-HATI: Script ini akan HAPUS semua data di tabel Indonesia!
-- ====================================

-- Drop tabel Indonesia jika sudah ada tabel Inggris
DO $$ 
BEGIN
    -- Drop pengguna jika users sudah ada
    IF EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'users') 
       AND EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'pengguna') THEN
        DROP TABLE IF EXISTS pengguna CASCADE;
        RAISE NOTICE 'Table pengguna dropped (users already exists)';
    END IF;

    -- Drop pelanggan jika customers sudah ada
    IF EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'customers') 
       AND EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'pelanggan') THEN
        DROP TABLE IF EXISTS pelanggan CASCADE;
        RAISE NOTICE 'Table pelanggan dropped (customers already exists)';
    END IF;

    -- Drop pesanan jika orders sudah ada
    IF EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'orders') 
       AND EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'pesanan') THEN
        DROP TABLE IF EXISTS pesanan CASCADE;
        RAISE NOTICE 'Table pesanan dropped (orders already exists)';
    END IF;

    -- Drop tagihan jika billings sudah ada
    IF EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'billings') 
       AND EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'tagihan') THEN
        DROP TABLE IF EXISTS tagihan CASCADE;
        RAISE NOTICE 'Table tagihan dropped (billings already exists)';
    END IF;

    -- Drop pesan_obrolan jika chat_messages sudah ada
    IF EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'chat_messages') 
       AND EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'pesan_obrolan') THEN
        DROP TABLE IF EXISTS pesan_obrolan CASCADE;
        RAISE NOTICE 'Table pesan_obrolan dropped (chat_messages already exists)';
    END IF;

    -- Drop lokasi_kurir jika courier_locations sudah ada
    IF EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'courier_locations') 
       AND EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'lokasi_kurir') THEN
        DROP TABLE IF EXISTS lokasi_kurir CASCADE;
        RAISE NOTICE 'Table lokasi_kurir dropped (courier_locations already exists)';
    END IF;

    -- Drop bukti_pembayaran jika payment_proofs sudah ada
    IF EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'payment_proofs') 
       AND EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'bukti_pembayaran') THEN
        DROP TABLE IF EXISTS bukti_pembayaran CASCADE;
        RAISE NOTICE 'Table bukti_pembayaran dropped (payment_proofs already exists)';
    END IF;
END $$;

