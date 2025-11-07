from fastapi import FastAPI, HTTPException, Depends, UploadFile, File, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List, Optional
import uvicorn
from datetime import datetime, timedelta
from pathlib import Path
import os

from database import get_db, engine
import models
import schemas
import crud
from auth import create_access_token, get_current_user, get_current_admin_user, require_role
from email_service import send_order_confirmation_email, send_order_assigned_email, send_order_completed_email, send_payment_proof_email
from file_upload import save_payment_proof, PAYMENT_PROOF_DIR

# Create database tables (with error handling)
# Skip in serverless environment (Vercel)
if not os.getenv("VERCEL"):
    try:
        models.Base.metadata.create_all(bind=engine)
        print("[OK] Database tables created successfully!")
    except Exception as e:
        print(f"[WARNING] Could not create database tables: {str(e)}")
        print("   Make sure PostgreSQL is running and database is created.")
        print("   You can create tables later using: python init_db.py")

app = FastAPI(
    title="JelantahGO - Used Cooking Oil Pickup Management",
    description="Complete pickup and management system for used cooking oil business",
    version="2.0.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files for serving uploaded files
# Skip in serverless environment (Vercel) - use external storage instead
if not os.getenv("VERCEL"):
    uploads_dir = Path("uploads")
    uploads_dir.mkdir(exist_ok=True)
    app.mount("/files", StaticFiles(directory="uploads"), name="files")

# =====================
# AUTHENTICATION ENDPOINTS
# =====================

@app.post("/auth/register", response_model=schemas.User)
def register_user(request: schemas.UserRegister, db: Session = Depends(get_db)):
    """Register a new user"""
    user = crud.create_user(db, request)
    if not user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user

@app.post("/auth/login", response_model=schemas.Token)
def login_user(request: schemas.UserLogin, db: Session = Depends(get_db)):
    """Login user and get access token"""
    user = crud.authenticate_user(db, request.email, request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Update last login
    crud.update_user_last_login(db, user.id)
    
    # Create access token
    access_token = create_access_token(data={"sub": user.id, "role": user.role})
    
    return schemas.Token(
        access_token=access_token,
        token_type="bearer",
        user_id=user.id,
        role=user.role,
        name=user.name
    )

@app.get("/auth/me", response_model=schemas.User)
def get_current_user_info(current_user: models.User = Depends(get_current_user)):
    """Get current authenticated user info"""
    return current_user

# =====================
# ROOT ENDPOINT
# =====================

@app.get("/")
def root():
    """Root endpoint - redirects to API documentation"""
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/docs")

# =====================
# DASHBOARD ENDPOINTS
# =====================

@app.post("/dashboard", response_model=schemas.DashboardResponse)
def get_dashboard(request: schemas.DashboardRequest, db: Session = Depends(get_db)):
    """Get role-specific dashboard summary"""
    if request.role == "admin":
        summary = crud.get_admin_summary(db)
    elif request.role == "customer" and request.user_id:
        summary = crud.get_customer_summary(db, request.user_id)
    elif request.role == "courier" and request.user_id:
        summary = crud.get_courier_summary(db, request.user_id)
    else:
        summary = {"total_inventory": 0, "pending_deliveries": 0}
    
    return schemas.DashboardResponse(
        message=f"Welcome to JelantahGO {request.role} dashboard",
        role=request.role,
        summary=summary
    )

# =====================
# CUSTOMER ENDPOINTS
# =====================

@app.post("/customer/register", response_model=schemas.CustomerResponse)
def register_customer(request: schemas.CustomerCreate, db: Session = Depends(get_db)):
    """Register a new customer"""
    # Check if email already exists
    existing = crud.get_customer_by_email(db, request.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    customer = crud.create_customer(db, request)
    return schemas.CustomerResponse(
        success=True,
        customer_id=customer.id,
        customer=customer,
        message=f"Customer {request.name} registered successfully!"
    )

@app.get("/customer/{customer_id}", response_model=schemas.Customer)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    """Get customer by ID"""
    customer = crud.get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

# =====================
# ORDER ENDPOINTS
# =====================

@app.post("/order/create", response_model=schemas.OrderResponse)
def create_order(request: schemas.OrderCreate, db: Session = Depends(get_db)):
    """Create a new pickup order"""
    customer = crud.get_customer(db, request.customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    order = crud.create_order(db, request, customer)
    
    # Send confirmation email
    try:
        send_order_confirmation_email(customer.email, customer.name, order.id)
    except Exception as e:
        print(f"Error sending email: {str(e)}")
    
    return schemas.OrderResponse(
        success=True,
        order_id=order.id,
        order=order,
        message="Pickup request created successfully!"
    )

@app.post("/order/assign", response_model=schemas.OrderAssignResponse)
def assign_courier(
    request: schemas.OrderAssign, 
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    """Assign courier to order (Admin only)"""
    order = crud.assign_courier_to_order(db, request.order_id, request.courier_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    # Send email notification
    try:
        customer = crud.get_customer(db, order.customer_id)
        if customer:
            send_order_assigned_email(customer.email, customer.name, order.id, order.courier_name or f"Courier {request.courier_id}")
    except Exception as e:
        print(f"Error sending email: {str(e)}")
    
    return schemas.OrderAssignResponse(
        success=True,
        order=order,
        message=f"Order assigned to courier {request.courier_id}"
    )

@app.post("/order/update-status", response_model=schemas.OrderStatusResponse)
def update_order_status(request: schemas.OrderStatusUpdate, db: Session = Depends(get_db)):
    """Update order status and calculate billing"""
    order = crud.update_order_status(db, request)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    billing = None
    if request.new_status == "completed" and request.volume_liters:
        billing = crud.get_billing_by_order(db, request.order_id)
        
        # Send completion email
        try:
            customer = crud.get_customer(db, order.customer_id)
            if customer and billing:
                send_order_completed_email(customer.email, customer.name, order.id, billing.grand_total)
        except Exception as e:
            print(f"Error sending email: {str(e)}")
    
    return schemas.OrderStatusResponse(
        success=True,
        order=order,
        billing=billing,
        message=f"Order status updated to {request.new_status}"
    )

@app.post("/order/list", response_model=schemas.OrderListResponse)
def list_orders(request: schemas.OrderListRequest, db: Session = Depends(get_db)):
    """List orders filtered by role"""
    orders = crud.get_orders_by_role(
        db,
        role=request.role,
        user_id=request.user_id,
        status_filter=request.status_filter,
        limit=request.limit
    )
    return schemas.OrderListResponse(
        orders=orders,
        total_count=len(orders)
    )

@app.get("/order/{order_id}", response_model=schemas.Order)
def get_order(order_id: int, db: Session = Depends(get_db)):
    """Get order by ID"""
    order = crud.get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

# =====================
# LOCATION ENDPOINTS
# =====================

@app.post("/location/update", response_model=schemas.LocationUpdateResponse)
def update_location(request: schemas.LocationUpdate, db: Session = Depends(get_db)):
    """Update courier location"""
    location = crud.update_courier_location(db, request)
    return schemas.LocationUpdateResponse(
        success=True,
        message="Location updated successfully"
    )

@app.post("/location/get", response_model=schemas.LocationResponse)
def get_location(request: schemas.LocationGet, db: Session = Depends(get_db)):
    """Get courier location for order"""
    location = crud.get_courier_location(db, request.order_id)
    if not location:
        return schemas.LocationResponse(
            courier_id=None,
            courier_name=None,
            location=None,
            last_updated=None,
            eta_minutes=None
        )
    
    return location

# =====================
# CHAT ENDPOINTS
# =====================

@app.post("/chat/send", response_model=schemas.ChatSendResponse)
def send_chat_message(request: schemas.ChatSend, db: Session = Depends(get_db)):
    """Send chat message"""
    message = crud.create_chat_message(db, request)
    return schemas.ChatSendResponse(
        success=True,
        message_id=message.id,
        timestamp=message.timestamp.isoformat()
    )

@app.post("/chat/get", response_model=schemas.ChatGetResponse)
def get_chat_messages(request: schemas.ChatGet, db: Session = Depends(get_db)):
    """Get chat messages for order"""
    messages = crud.get_chat_messages(db, request.order_id, request.limit)
    return schemas.ChatGetResponse(
        messages=messages,
        total_count=len(messages)
    )

# =====================
# BILLING ENDPOINTS
# =====================

@app.post("/billing/calculate", response_model=schemas.BillingResponse)
def get_billing(request: schemas.BillingGet, db: Session = Depends(get_db)):
    """Get billing details for completed order"""
    billing = crud.get_billing_by_order(db, request.order_id)
    if not billing:
        raise HTTPException(status_code=404, detail="Billing data not found")
    
    breakdown = {
        "volume_liters": billing.volume_liters,
        "price_per_liter": f"Rp{billing.base_price_per_liter:,.0f}",
        "base_total": f"Rp{billing.base_total:,.0f}",
        "courier_fee": f"Rp{billing.courier_fee:,.0f}",
        "affiliate_fee": f"Rp{billing.affiliate_fee:,.0f}",
        "grand_total": f"Rp{billing.grand_total:,.0f}",
        "payment_status": "Paid" if billing.paid else "Pending"
    }
    
    return schemas.BillingResponse(
        billing=billing,
        breakdown=breakdown
    )

# =====================
# FILE UPLOAD ENDPOINTS
# =====================

@app.post("/payment-proof/upload", response_model=schemas.PaymentProofUploadResponse)
async def upload_payment_proof(
    order_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_admin_user)
):
    """Upload payment proof for order (Admin only)"""
    # Verify order exists
    order = crud.get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    # Save file
    file_info = await save_payment_proof(file, order_id)
    
    # Create payment proof record
    payment_proof = crud.create_payment_proof(
        db=db,
        order_id=order_id,
        file_path=file_info["file_path"],
        file_name=file_info["file_name"],
        file_size=file_info["file_size"],
        uploaded_by=current_user.id
    )
    
    # Get payment proof URL
    from file_upload import get_payment_proof_url
    proof_url = get_payment_proof_url(file_info["file_path"])
    
    # Send email notification
    try:
        customer = crud.get_customer(db, order.customer_id)
        if customer:
            send_payment_proof_email(customer.email, customer.name, order_id, proof_url)
    except Exception as e:
        print(f"Error sending email: {str(e)}")
    
    return schemas.PaymentProofUploadResponse(
        success=True,
        message="Payment proof uploaded successfully",
        payment_proof=schemas.PaymentProofResponse(
            id=payment_proof.id,
            order_id=payment_proof.order_id,
            file_name=payment_proof.file_name,
            file_url=proof_url,
            file_size=payment_proof.file_size,
            uploaded_at=payment_proof.uploaded_at
        )
    )

@app.get("/payment-proof/{order_id}", response_model=List[schemas.PaymentProofResponse])
def get_payment_proofs(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    """Get payment proofs for an order"""
    # Verify order exists
    order = crud.get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    # Check access: customer can only see their own orders
    if current_user.role == "customer" and order.customer_id != current_user.customer_id:
        raise HTTPException(status_code=403, detail="Access denied")
    
    proofs = crud.get_payment_proofs_by_order(db, order_id)
    return proofs

# =====================
# HEALTH CHECK
# =====================

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "JelantahGO Backend"}

if __name__ == "__main__":
    import os
    host = os.getenv("API_HOST", "0.0.0.0")
    # Railway uses PORT env var automatically, fallback to API_PORT or 8000
    port = int(os.getenv("PORT", os.getenv("API_PORT", 8000)))
    uvicorn.run(app, host=host, port=port)
