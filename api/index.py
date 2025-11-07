"""
Vercel serverless function for FastAPI
This file is for deploying FastAPI to Vercel as serverless functions
"""
import os

# Set VERCEL environment variable to skip certain operations
os.environ["VERCEL"] = "1"

from mangum import Mangum
from main import app

# Wrap FastAPI app with Mangum for Vercel
handler = Mangum(app, lifespan="off")
