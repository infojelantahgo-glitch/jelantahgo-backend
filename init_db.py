"""
Database initialization script
Run this once to create all tables
"""

from database import engine
import models

def init_database():
    """Create all database tables"""
    print("Creating database tables...")
    models.Base.metadata.create_all(bind=engine)
    print("[OK] Database tables created successfully!")

if __name__ == "__main__":
    init_database()
