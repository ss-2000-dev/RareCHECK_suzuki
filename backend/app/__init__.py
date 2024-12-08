from flask import Flask
from flask_cors import CORS
from flask_session import Session
from app.models import db
from app.config import Config

def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    Session(app)

    # Register Blueprints
    from app.routes.admin import admin_bp
    from app.routes.auth import auth_bp
    from app.routes.questions import questions_bp
    from app.routes.users import users_bp

    app.register_blueprint(admin_bp, url_prefix='/rarecheck/admin')
    app.register_blueprint(auth_bp, url_prefix='/rarecheck/users')
    app.register_blueprint(questions_bp, url_prefix='/rarecheck/questions')
    app.register_blueprint(users_bp, url_prefix='/rarecheck/users')

    return app