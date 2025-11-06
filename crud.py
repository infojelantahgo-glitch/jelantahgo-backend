from sqlalchemy.orm import Session
from datetime import datetime
import models
import schemas
from auth import get_password_hash, verify_password
from file_upload import get_payment_proof_url

# Pricing configuration
PRICING_TIERS = [
    (1, 99, 6500),
    (100, 200, 7000),
    (201, float('inf'), 7500)
]
COURIER_FEE_PER_LITER = 1000
AFFILIATE_FEE_PER_LITER = 200

def calculate_price_per_liter(volume: float) -> float:
    """Calculate price per liter based on volume"""
    for min_vol, max_vol, price in PRICING_TIERS:
        if min_vol <= volume <= max_vol:
            return price
    return PRICING_TIERS[-1][2]

def calculate_billing(volume_liters: float, has_referrer: bool) -> dict:
    """Calculate billing breakdown"""
    price_per_liter = calculate_price_per_liter(volume_liters)
    base_total = volume_liters * price_per_liter
    courier_fee = volume_liters * COURIER_FEE_PER_LITER
    affiliate_fee = volume_liters * AFFILIATE_FEE_PER_LITER if has_referrer else 0
    
    return {
        "base_price_per_liter": price_per_liter,
        "base_total": base_total,
        "courier_fee": courier_fee,
        "affiliate_fee": affiliate_fee,
        "grand_total": base_total + courier_fee + affiliate_fee
    }

# =====================
# Customer CRUD
# =====================

def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()

def get_customer_by_email(db: Session, email: str):
    return db.query(models.Customer).filter(models.Customer.email == email).first()

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

# =====================
# Order CRUD
# =====================

def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def create_order(db: Session, order: schemas.OrderCreate, customer: models.Customer):
    db_order = models.Order(
        customer_id=order.customer_id,
        customer_name=customer.name,
        address=order.address or customer.address,
        status="pending"
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def assign_courier_to_order(db: Session, order_id: int, courier_id: int):
    order = get_order(db, order_id)
    if order:
        order.courier_id = courier_id
        order.courier_name = f"Courier {courier_id}"
        order.status = "assigned"
        order.pickup_date = datetime.utcnow()
        db.commit()
        db.refresh(order)
    return order

def update_order_status(db: Session, request: schemas.OrderStatusUpdate):
    order = get_order(db, request.order_id)
    if not order:
        return None
    
    order.status = request.new_status
    
    # If completing order, create billing
    if request.new_status == "completed" and request.volume_liters:
        order.volume_liters = request.volume_liters
        order.completed_at = datetime.utcnow()
        
        # Check if customer has referrer
        customer = get_customer(db, order.customer_id)
        has_referrer = bool(customer.referrer_id)
        
        # Calculate billing
        billing_calc = calculate_billing(request.volume_liters, has_referrer)
        
        # Create billing record
        db_billing = models.Billing(
            order_id=request.order_id,
            volume_liters=request.volume_liters,
            **billing_calc
        )
        db.add(db_billing)
    
    db.commit()
    db.refresh(order)
    return order

def get_orders_by_role(db: Session, role: str, user_id: int = None, 
                       status_filter: str = None, limit: int = 50):
    query = db.query(models.Order)
    
    if role == "customer" and user_id:
        query = query.filter(models.Order.customer_id == user_id)
    elif role == "courier" and user_id:
        query = query.filter(models.Order.courier_id == user_id)
    
    if status_filter:
        query = query.filter(models.Order.status == status_filter)
    
    return query.order_by(models.Order.created_at.desc()).limit(limit).all()

# =====================
# Billing CRUD
# =====================

def get_billing_by_order(db: Session, order_id: int):
    return db.query(models.Billing).filter(models.Billing.order_id == order_id).first()

# =====================
# Location CRUD
# =====================

def update_courier_location(db: Session, request: schemas.LocationUpdate):
    location = db.query(models.CourierLocation).filter(
        models.CourierLocation.order_id == request.order_id
    ).first()
    
    if location:
        location.courier_id = request.courier_id
        location.latitude = request.latitude
        location.longitude = request.longitude
        location.eta_minutes = request.eta_minutes
        location.last_updated = datetime.utcnow()
    else:
        location = models.CourierLocation(**request.model_dump())
        db.add(location)
    
    db.commit()
    db.refresh(location)
    return location

def get_courier_location(db: Session, order_id: int):
    location = db.query(models.CourierLocation).filter(
        models.CourierLocation.order_id == order_id
    ).first()
    
    if not location:
        return None
    
    order = get_order(db, order_id)
    
    return schemas.LocationResponse(
        courier_id=location.courier_id,
        courier_name=order.courier_name if order else None,
        location={
            "latitude": location.latitude,
            "longitude": location.longitude
        },
        last_updated=location.last_updated,
        eta_minutes=location.eta_minutes
    )

# =====================
# Chat CRUD
# =====================

def create_chat_message(db: Session, request: schemas.ChatSend):
    message = models.ChatMessage(**request.model_dump())
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

def get_chat_messages(db: Session, order_id: int, limit: int = 50):
    return db.query(models.ChatMessage).filter(
        models.ChatMessage.order_id == order_id
    ).order_by(models.ChatMessage.timestamp.asc()).limit(limit).all()

# =====================
# Dashboard CRUD
# =====================

def get_admin_summary(db: Session):
    total_orders = db.query(models.Order).count()
    pending_orders = db.query(models.Order).filter(
        models.Order.status == "pending"
    ).count()
    
    return {
        "total_orders": total_orders,
        "pending_orders": pending_orders,
        "active_couriers": 0
    }

def get_customer_summary(db: Session, customer_id: int):
    total_orders = db.query(models.Order).filter(
        models.Order.customer_id == customer_id
    ).count()
    
    last_order = db.query(models.Order).filter(
        models.Order.customer_id == customer_id
    ).order_by(models.Order.created_at.desc()).first()
    
    return {
        "total_orders": total_orders,
        "last_order_status": last_order.status if last_order else None
    }

def get_courier_summary(db: Session, courier_id: int):
    assigned_orders = db.query(models.Order).filter(
        models.Order.courier_id == courier_id
    ).count()
    
    active_orders = db.query(models.Order).filter(
        models.Order.courier_id == courier_id
    ).filter(
        models.Order.status.in_(["assigned", "in_progress"])
    ).count()
    
    return {
        "assigned_orders": assigned_orders,
        "active_orders": active_orders
    }

# =====================
# User CRUD
# =====================

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserRegister):
    # Check if email already exists
    existing = get_user_by_email(db, user.email)
    if existing:
        return None
    
    db_user = models.User(
        email=user.email,
        password_hash=get_password_hash(user.password),
        name=user.name,
        role=user.role,
        phone=user.phone,
        customer_id=user.customer_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    if not user.is_active:
        return None
    return user

def update_user_last_login(db: Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        user.last_login = datetime.utcnow()
        db.commit()
        db.refresh(user)
    return user

# =====================
# Payment Proof CRUD
# =====================

def create_payment_proof(db: Session, order_id: int, file_path: str, file_name: str, file_size: int, uploaded_by: int):
    db_proof = models.PaymentProof(
        order_id=order_id,
        file_path=file_path,
        file_name=file_name,
        file_size=file_size,
        uploaded_by=uploaded_by
    )
    db.add(db_proof)
    
    # Update billing paid status
    billing = get_billing_by_order(db, order_id)
    if billing:
        billing.paid = True
    
    db.commit()
    db.refresh(db_proof)
    return db_proof

def get_payment_proofs_by_order(db: Session, order_id: int):
    proofs = db.query(models.PaymentProof).filter(
        models.PaymentProof.order_id == order_id
    ).order_by(models.PaymentProof.uploaded_at.desc()).all()
    
    result = []
    for proof in proofs:
        result.append({
            "id": proof.id,
            "order_id": proof.order_id,
            "file_name": proof.file_name,
            "file_url": get_payment_proof_url(proof.file_path),
            "file_size": proof.file_size,
            "uploaded_at": proof.uploaded_at
        })
    return result

def get_payment_proof(db: Session, proof_id: int):
    return db.query(models.PaymentProof).filter(models.PaymentProof.id == proof_id).first()
