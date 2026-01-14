from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.routes.main.inicio import inicio
    from app.routes.others.others import others

    app.register_blueprint(inicio)
    app.register_blueprint(others)

    return app