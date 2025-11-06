from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

# =====================
# Customer Schemas
# =====================

class CustomerBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: str
    referrer_id: Optional[int] = None

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class CustomerResponse(BaseModel):
    success: bool
    customer_id: int
    customer: Customer
    message: str

# =====================
# Order Schemas
# =====================

class OrderCreate(BaseModel):
    customer_id: int
    address: Optional[str] = None
    notes: Optional[str] = None

class OrderAssign(BaseModel):
    order_id: int
    courier_id: int

class OrderStatusUpdate(BaseModel):
    order_id: int
    new_status: str
    volume_liters: Optional[float] = None
    courier_id: Optional[int] = None

class OrderListRequest(BaseModel):
    role: str
    user_id: Optional[int] = None
    status_filter: Optional[str] = None
    limit: int = 50

class Order(BaseModel):
    id: int
    customer_id: int
    customer_name: str
    courier_id: Optional[int] = None
    courier_name: Optional[str] = None
    volume_liters: Optional[float] = None
    status: str
    address: str
    created_at: datetime
    pickup_date: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class OrderResponse(BaseModel):
    success: bool
    order_id: int
    order: Order
    message: str

class OrderAssignResponse(BaseModel):
    success: bool
    order: Order
    message: str

# =====================
# Billing Schemas
# =====================

class Billing(BaseModel):
    id: int
    order_id: int
    volume_liters: float
    base_price_per_liter: float
    base_total: float
    courier_fee: float
    affiliate_fee: float
    grand_total: float
    paid: bool
    
    class Config:
        from_attributes = True

class OrderStatusResponse(BaseModel):
    success: bool
    order: Order
    billing: Optional[Billing] = None
    message: str

class OrderListResponse(BaseModel):
    orders: List[Order]
    total_count: int

class BillingGet(BaseModel):
    order_id: int

class BillingResponse(BaseModel):
    billing: Billing
    breakdown: dict

# =====================
# Location Schemas
# =====================

class LocationUpdate(BaseModel):
    courier_id: int
    order_id: int
    latitude: float
    longitude: float
    eta_minutes: Optional[int] = None

class LocationGet(BaseModel):
    order_id: int

class LocationUpdateResponse(BaseModel):
    success: bool
    message: str

class LocationResponse(BaseModel):
    courier_id: Optional[int]
    courier_name: Optional[str]
    location: Optional[dict]
    last_updated: Optional[datetime]
    eta_minutes: Optional[int]

# =====================
# Chat Schemas
# =====================

class ChatSend(BaseModel):
    order_id: int
    sender_role: str
    sender_name: str
    message: str

class ChatGet(BaseModel):
    order_id: int
    limit: int = 50

class ChatMessage(BaseModel):
    id: int
    order_id: int
    sender_role: str
    sender_name: str
    message: str
    timestamp: datetime
    
    class Config:
        from_attributes = True

class ChatSendResponse(BaseModel):
    success: bool
    message_id: int
    timestamp: str

class ChatGetResponse(BaseModel):
    messages: List[ChatMessage]
    total_count: int

# =====================
# Dashboard Schemas
# =====================

class DashboardRequest(BaseModel):
    role: str
    user_id: Optional[int] = None

class DashboardResponse(BaseModel):
    message: str
    role: str
    summary: dict

# =====================
# Authentication Schemas
# =====================

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserRegister(BaseModel):
    email: EmailStr
    password: str
    name: str
    role: str = "customer"  # admin, customer, courier, warehouse
    phone: Optional[str] = None
    customer_id: Optional[int] = None

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user_id: int
    role: str
    name: str

class User(BaseModel):
    id: int
    email: str
    role: str
    name: str
    phone: Optional[str] = None
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# =====================
# File Upload Schemas
# =====================

class PaymentProofResponse(BaseModel):
    id: int
    order_id: int
    file_name: str
    file_url: str
    file_size: Optional[int] = None
    uploaded_at: datetime
    
    class Config:
        from_attributes = True

class PaymentProofUploadResponse(BaseModel):
    success: bool
    message: str
    payment_proof: PaymentProofResponse
