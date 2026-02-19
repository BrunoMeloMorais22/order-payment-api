from flask import Blueprint, request, jsonify
from extensions import db
from models import Order
from flask_jwt_extended import jwt_required, get_jwt_identity

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/", methods=["POST"])
@jwt_required()
def create_order():
    data = request.get_json()
    user_id = get_jwt_identity()

    order = Order(
        amount=data["amount"],
        user_id=user_id
    )

    db.session.add(order)
    db.session.commit()

    return jsonify({
        "id": order.id,
        "amount": order.amount,
        "status": order.status
    }), 201


@orders_bp.route("/", methods=["GET"])
@jwt_required()
def list_orders():
    user_id = get_jwt_identity()
    orders = Order.query.filter_by(user_id=user_id).all()

    return jsonify([
        {
            "id": o.id,
            "amount": o.amount,
            "status": o.status
        } for o in orders
    ])
