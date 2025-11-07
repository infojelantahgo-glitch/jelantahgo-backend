from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Database URL
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://jelantahgo:jelantahgo123@localhost/jelantahgo_db"
)

# Create engine with connection pooling for serverless
# Use pool_pre_ping to handle connection issues in serverless environment
try:
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,  # Verify connections before using
        pool_recycle=300,    # Recycle connections after 5 minutes
        echo=False           # Disable SQL logging
    )
except Exception as e:
    # If engine creation fails, create a dummy engine
    # This will fail on actual use but allows import to succeed
    print(f"WARNING: Failed to create database engine: {str(e)}")
    engine = None

# Create SessionLocal class
if engine:
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
else:
    SessionLocal = None

# Create Base class
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
