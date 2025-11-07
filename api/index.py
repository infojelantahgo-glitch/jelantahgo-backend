"""
Vercel serverless function for FastAPI
This file is for deploying FastAPI to Vercel as serverless functions
"""
import os
import sys
import json
import traceback
from pathlib import Path

# Add parent directory to Python path so we can import from root
# Vercel functions run from /var/task/api/, so we need to add parent to path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

# Log path information for debugging
print(f"[DEBUG] Current directory: {current_dir}", file=sys.stderr)
print(f"[DEBUG] Parent directory: {parent_dir}", file=sys.stderr)
print(f"[DEBUG] Python path: {sys.path[:3]}", file=sys.stderr)

# Set VERCEL environment variable to skip certain operations
os.environ["VERCEL"] = "1"

# Initialize handler variable
handler = None
import_error = None
import_step = "initialization"

def log_error(step, error, exc_info=None):
    """Log error with detailed information"""
    global import_error
    import_error = f"[{step}] {str(error)}"
    print(f"[ERROR] {import_error}", file=sys.stderr)
    if exc_info:
        traceback.print_exception(*exc_info, file=sys.stderr)
    else:
        traceback.print_exc(file=sys.stderr)

# Step 1: Import mangum
import_step = "mangum_import"
try:
    from mangum import Mangum
    print("[OK] Step 1: Mangum imported successfully", file=sys.stderr)
except Exception as e:
    log_error(import_step, e, sys.exc_info())
    Mangum = None

# Step 2: Import database (with error handling)
if Mangum:
    import_step = "database_import"
    try:
        from database import get_db, engine, SessionLocal
        print("[OK] Step 2: Database module imported successfully", file=sys.stderr)
        if engine is None:
            print("[WARNING] Database engine is None - DATABASE_URL may not be set", file=sys.stderr)
    except Exception as e:
        log_error(import_step, e, sys.exc_info())
        # Continue anyway - database might not be needed for basic health check

# Step 3: Import models
if Mangum:
    import_step = "models_import"
    try:
        import models
        print("[OK] Step 3: Models imported successfully", file=sys.stderr)
    except Exception as e:
        log_error(import_step, e, sys.exc_info())
        models = None

# Step 4: Import schemas
if Mangum and models:
    import_step = "schemas_import"
    try:
        import schemas
        print("[OK] Step 4: Schemas imported successfully", file=sys.stderr)
    except Exception as e:
        log_error(import_step, e, sys.exc_info())
        schemas = None

# Step 5: Import crud
if Mangum and models and schemas:
    import_step = "crud_import"
    try:
        import crud
        print("[OK] Step 5: CRUD imported successfully", file=sys.stderr)
    except Exception as e:
        log_error(import_step, e, sys.exc_info())
        crud = None

# Step 6: Import auth
if Mangum and models and schemas and crud:
    import_step = "auth_import"
    try:
        from auth import create_access_token, get_current_user, get_current_admin_user, require_role
        print("[OK] Step 6: Auth imported successfully", file=sys.stderr)
    except Exception as e:
        log_error(import_step, e, sys.exc_info())
        # Continue - some endpoints might work without auth

# Step 7: Import email_service
if Mangum:
    import_step = "email_service_import"
    try:
        from email_service import send_order_confirmation_email, send_order_assigned_email, send_order_completed_email, send_payment_proof_email
        print("[OK] Step 7: Email service imported successfully", file=sys.stderr)
    except Exception as e:
        log_error(import_step, e, sys.exc_info())
        # Continue - email is optional

# Step 8: Import file_upload
if Mangum:
    import_step = "file_upload_import"
    try:
        from file_upload import save_payment_proof, PAYMENT_PROOF_DIR
        print("[OK] Step 8: File upload imported successfully", file=sys.stderr)
    except Exception as e:
        log_error(import_step, e, sys.exc_info())
        # Continue - file upload is optional

# Step 9: Import main app
if Mangum:
    import_step = "main_app_import"
    try:
        from main import app
        print("[OK] Step 9: FastAPI app imported successfully", file=sys.stderr)
        
        # Step 10: Create Mangum handler
        import_step = "mangum_handler_creation"
        handler = Mangum(app, lifespan="off")
        print("[OK] Step 10: Mangum handler created successfully", file=sys.stderr)
        print("[SUCCESS] All imports completed - handler ready!", file=sys.stderr)
    except Exception as e:
        log_error(import_step, e, sys.exc_info())

# Create error handler if import failed
if handler is None:
    def handler(event, context):
        """Fallback error handler"""
        error_msg = import_error or "Unknown error during initialization"
        
        # Log error details
        print(f"[ERROR] Handler called but app failed to initialize", file=sys.stderr)
        print(f"[ERROR] Last failed step: {import_step}", file=sys.stderr)
        print(f"[ERROR] Error: {error_msg}", file=sys.stderr)
        if isinstance(event, dict):
            print(f"[ERROR] Event path: {event.get('path', 'unknown')}", file=sys.stderr)
            print(f"[ERROR] Event method: {event.get('httpMethod', 'unknown')}", file=sys.stderr)
        
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps({
                "error": "Internal Server Error",
                "message": "Application failed to initialize",
                "detail": error_msg,
                "step": import_step,
                "path": event.get("path", "unknown") if isinstance(event, dict) else "unknown"
            })
        }
