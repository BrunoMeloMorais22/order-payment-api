from flask import Blueprint, request, jsonify
from extensions import db, bcrypt
from models import User
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    hashed_password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")

    user = User(
        email = data["email"],
        password = hashed_password
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Usuário criado"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user = User.query.filter_by(email=data["email"]).first()
    
    if not user or not bcrypt.check_password_hash(user.password, data["password"]):
        return jsonify({"error": "Credenciais inválidas"}), 401
    
    access_token = create_access_token(identity=user.id)

    return jsonify({"access_token": access_token}), 200