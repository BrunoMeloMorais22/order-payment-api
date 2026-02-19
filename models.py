import uuid
from datetime import datetime
from extensions import db

def generate_uuid():
    return str(uuid.uuid4())

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    orders = db.relationship("Order", backref="user", lazy=True)


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default="PENDING")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)

    payments = db.relationship("Payment", backref="order", lazy=True)


class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    payment_intent_id = db.Column(db.String(100), unique=True, nullable=False)
    client_secret = db.Column(db.String(200), nullable=False)

    status = db.Column(db.String(50), default="requires_payment_method")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    order_id = db.Column(db.String(36), db.ForeignKey("orders.id"), nullable=False)