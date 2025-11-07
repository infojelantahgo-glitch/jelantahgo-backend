"""
Vercel serverless function for FastAPI
This file is for deploying FastAPI to Vercel as serverless functions
"""
import os
import sys
import json

# Set VERCEL environment variable to skip certain operations
os.environ["VERCEL"] = "1"

# Initialize handler variable
handler = None
import_error = None

# Try to import with detailed error handling
try:
    # Import mangum first
    from mangum import Mangum
    print("[OK] Mangum imported successfully", file=sys.stderr)
except ImportError as e:
    import_error = f"Failed to import Mangum: {str(e)}"
    print(f"[ERROR] {import_error}", file=sys.stderr)
    import traceback
    traceback.print_exc(file=sys.stderr)

if not import_error:
    try:
        # Import main app
        from main import app
        print("[OK] FastAPI app imported successfully", file=sys.stderr)
        
        # Wrap FastAPI app with Mangum for Vercel
        handler = Mangum(app, lifespan="off")
        print("[OK] Mangum handler created successfully", file=sys.stderr)
    except Exception as e:
        import_error = f"Failed to import or create app: {str(e)}"
        print(f"[ERROR] {import_error}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)

# Create error handler if import failed
if handler is None:
    def handler(event, context):
        """Fallback error handler"""
        error_msg = import_error or "Unknown error during initialization"
        
        # Log error details
        print(f"[ERROR] Handler called but app failed to initialize: {error_msg}", file=sys.stderr)
        print(f"[ERROR] Event: {json.dumps(event, default=str)}", file=sys.stderr)
        
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
                "path": event.get("path", "unknown") if isinstance(event, dict) else "unknown"
            })
        }
