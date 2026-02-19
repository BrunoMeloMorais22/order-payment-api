from flask import Flask
from config import Config
from extensions import db, jwt, bcrypt

from routes.auth import auth_bp
from routes.orders import orders_bp
from routes.payments import payments_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(orders_bp, url_prefix="/orders")
    app.register_blueprint(payments_bp, url_prefix="/payments")

    @app.route("/")
    def home():
        return {"message": "API de pagamento rodando"}, 200
    
    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
