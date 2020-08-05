from flask import Flask
from flask_login import  LoginManager
from flask_sqlalchemy import SQLAlchemy


login_manager = LoginManager()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '5eb861997206962e77f24379ea1b2552fc85769bf72843bf813a6578ee6a01c4'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:masterkey@localhost:5432/miniblog'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    login_manager.init_app(app)
    login_manager.login_view = "login"

    db.init_app(app)

     # Registro de los Blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp)
    from .admin import admin_bp
    app.register_blueprint(admin_bp)
    from .public import public_bp
    app.register_blueprint(public_bp)
    
    return app   