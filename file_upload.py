import os
import uuid
from pathlib import Path
from fastapi import UploadFile, HTTPException
from typing import Optional

# Upload configuration
UPLOAD_DIR = Path("uploads")
PAYMENT_PROOF_DIR = UPLOAD_DIR / "payment_proofs"
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".pdf"}

# Create upload directories (skip in Vercel - use external storage)
if not os.getenv("VERCEL"):
    try:
        UPLOAD_DIR.mkdir(exist_ok=True)
        PAYMENT_PROOF_DIR.mkdir(exist_ok=True)
    except Exception as e:
        print(f"[WARNING] Could not create upload directories: {str(e)}")

def get_file_extension(filename: str) -> str:
    """Get file extension from filename"""
    return Path(filename).suffix.lower()

def is_allowed_file(filename: str) -> bool:
    """Check if file extension is allowed"""
    ext = get_file_extension(filename)
    return ext in ALLOWED_EXTENSIONS

async def save_payment_proof(file: UploadFile, order_id: int) -> dict:
    """Save payment proof file and return file info"""
    # Validate file
    if not is_allowed_file(file.filename):
        raise HTTPException(
            status_code=400,
            detail=f"File type not allowed. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}"
        )
    
    # Read file content
    content = await file.read()
    file_size = len(content)
    
    # Check file size
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"File too large. Maximum size: {MAX_FILE_SIZE / 1024 / 1024} MB"
        )
    
    # Generate unique filename
    ext = get_file_extension(file.filename)
    unique_filename = f"order_{order_id}_{uuid.uuid4().hex}{ext}"
    file_path = PAYMENT_PROOF_DIR / unique_filename
    
    # Save file
    with open(file_path, "wb") as f:
        f.write(content)
    
    return {
        "file_path": str(file_path),
        "file_name": file.filename,
        "saved_filename": unique_filename,
        "file_size": file_size
    }

def get_payment_proof_url(file_path: str) -> str:
    """Generate URL for payment proof file"""
    # Convert to relative path for URL
    path_obj = Path(file_path)
    # Get filename only (file is already in payment_proofs directory)
    filename = path_obj.name
    return f"/files/payment_proofs/{filename}"

def delete_file(file_path: str) -> bool:
    """Delete a file"""
    try:
        path = Path(file_path)
        if path.exists():
            path.unlink()
            return True
        return False
    except Exception as e:
        print(f"Error deleting file {file_path}: {str(e)}")
        return False

