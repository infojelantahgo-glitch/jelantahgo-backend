from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False, index=True)  # admin, customer, courier, warehouse
    name = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)
    
    # Link to customer if role is customer
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)

class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    phone = Column(String(20), nullable=False)
    address = Column(Text, nullable=False)
    referrer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    orders = relationship("Order", back_populates="customer", foreign_keys="Order.customer_id")
    referrals = relationship("Customer", remote_side=[id])

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    customer_name = Column(String(100))
    courier_id = Column(Integer, nullable=True)
    courier_name = Column(String(100), nullable=True)
    volume_liters = Column(Float, nullable=True)
    status = Column(String(20), default="pending", index=True)
    address = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    pickup_date = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)
    
    # Relationships
    customer = relationship("Customer", back_populates="orders", foreign_keys=[customer_id])
    billing = relationship("Billing", back_populates="order", uselist=False)
    chat_messages = relationship("ChatMessage", back_populates="order")
    location = relationship("CourierLocation", back_populates="order", uselist=False)
    payment_proofs = relationship("PaymentProof", back_populates="order")

class Billing(Base):
    __tablename__ = "billings"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), unique=True, nullable=False)
    volume_liters = Column(Float, nullable=False)
    base_price_per_liter = Column(Float, nullable=False)
    base_total = Column(Float, nullable=False)
    courier_fee = Column(Float, nullable=False)
    affiliate_fee = Column(Float, nullable=False)
    grand_total = Column(Float, nullable=False)
    paid = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    order = relationship("Order", back_populates="billing")

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    sender_role = Column(String(20), nullable=False)
    sender_name = Column(String(100), nullable=False)
    message = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    
    # Relationships
    order = relationship("Order", back_populates="chat_messages")

class CourierLocation(Base):
    __tablename__ = "courier_locations"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), unique=True, nullable=False)
    courier_id = Column(Integer, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    eta_minutes = Column(Integer, nullable=True)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    order = relationship("Order", back_populates="location")

class PaymentProof(Base):
    __tablename__ = "payment_proofs"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    file_path = Column(String(500), nullable=False)
    file_name = Column(String(255), nullable=False)
    file_size = Column(Integer, nullable=True)  # in bytes
    uploaded_by = Column(Integer, ForeignKey("users.id"), nullable=False)  # admin user id
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    order = relationship("Order", back_populates="payment_proofs")
    uploader = relationship("User")
