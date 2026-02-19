import uuid
from flask import Blueprint, request, jsonify
from extensions import db
from models import Payment, Order
from flask_jwt_extended import jwt_required

payments_bp = Blueprint("payments", __name__)

def generate_payment_intent():
    return f"pi_{uuid.uuid4().hex[:24]}"

def generate_client_secret():
    return f"secret_{uuid.uuid4().hex}"


@payments_bp.route("/create-intent", methods=["POST"])
@jwt_required()
def create_payment_intent():
    data = request.get_json()

    if not data or "order_id" not in data:
        return jsonify({"error": "order_id is required"}), 400

    order = Order.query.get(data["order_id"])

    if not order:
        return jsonify({"error": "Order not found"}), 404

    payment = Payment(
        payment_intent_id=generate_payment_intent(),
        client_secret=generate_client_secret(),
        order_id=order.id
    )

    db.session.add(payment)
    db.session.commit()

    return jsonify({
        "payment_intent_id": payment.payment_intent_id,
        "client_secret": payment.client_secret,
        "status": payment.status
    }), 201


@payments_bp.route("/confirm", methods=["POST"])
@jwt_required()
def confirm_payment():
    data = request.get_json()

    payment = Payment.query.filter_by(
        payment_intent_id=data["payment_intent_id"]
    ).first()

    if not payment:
        return jsonify({"error": "Payment not found"}), 404

    payment.status = "succeeded"
    payment.order.status = "PAID"

    db.session.commit()

    return jsonify({"status": "succeeded"}), 200
