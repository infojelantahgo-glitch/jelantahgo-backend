"""
Vercel serverless function for FastAPI
This file is for deploying FastAPI to Vercel as serverless functions
"""
import os
import sys

# Set VERCEL environment variable to skip certain operations
os.environ["VERCEL"] = "1"

# Try to import with error handling
try:
    from mangum import Mangum
    from main import app
    
    # Wrap FastAPI app with Mangum for Vercel
    handler = Mangum(app, lifespan="off")
except Exception as e:
    # Print error for debugging
    print(f"ERROR: Failed to import app: {str(e)}", file=sys.stderr)
    import traceback
    traceback.print_exc(file=sys.stderr)
    
    # Create a minimal error handler
    def handler(event, context):
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
