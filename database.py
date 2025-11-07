from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import sys

# Only load dotenv if not in Vercel (Vercel uses environment variables directly)
if not os.getenv("VERCEL"):
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass  # dotenv not available, use environment variables

# Database URL
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://jelantahgo:jelantahgo123@localhost/jelantahgo_db"
)

# Create engine with connection pooling for serverless
# Use pool_pre_ping to handle connection issues in serverless environment
engine = None
SessionLocal = None

try:
    if DATABASE_URL and DATABASE_URL != "postgresql://jelantahgo:jelantahgo123@localhost/jelantahgo_db":
        engine = create_engine(
            DATABASE_URL,
            pool_pre_ping=True,  # Verify connections before using
            pool_recycle=300,    # Recycle connections after 5 minutes
            pool_size=1,         # Minimal pool size for serverless
            max_overflow=0,      # No overflow for serverless
            echo=False           # Disable SQL logging
        )
        print("[OK] Database engine created successfully", file=sys.stderr)
    else:
        print("[WARNING] DATABASE_URL not set, using default (may fail)", file=sys.stderr)
        engine = None
except Exception as e:
    # If engine creation fails, log but don't crash
    # This allows import to succeed even if DB is not configured
    print(f"[WARNING] Failed to create database engine: {str(e)}", file=sys.stderr)
    print(f"[WARNING] Database operations will fail until DATABASE_URL is configured", file=sys.stderr)
    engine = None

# Create SessionLocal class
if engine:
    try:
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        print("[OK] SessionLocal created successfully", file=sys.stderr)
    except Exception as e:
        print(f"[WARNING] Failed to create SessionLocal: {str(e)}", file=sys.stderr)
        SessionLocal = None
else:
    SessionLocal = None

# Create Base class (always available, even without DB connection)
Base = declarative_base()

# Dependency to get DB session
def get_db():
    if not SessionLocal:
        raise Exception("Database connection not configured. Please set DATABASE_URL environment variable.")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
