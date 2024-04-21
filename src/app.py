from config import Config

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from sqlalchemy import text

import logging
from datetime import datetime
import os


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    with app.app_context():
        db.init_app(app)

    jwt.init_app(app)
    cors.init_app(app)
    migrate.init_app(app)

    from errors import bp as errors_bp
    from users import bp as users_bp
    from auth import bp as auth_bp

    app.register_blueprint(errors_bp)
    app.register_blueprint(users_bp, url_prefix="/api/users")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    log_format = '%(name)s - %(levelname)s - %(message)s'
    nome_arquivo_log = str(datetime.now()).replace(" ", "-").replace(":", "-") + ".log"

    log_folder = 'logs'
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    logging.basicConfig(filename=f"./logs/{nome_arquivo_log}", filemode='a+', format=log_format, level=logging.INFO,encoding="utf-8")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    console_formatter = logging.Formatter(log_format)
    console_handler.setFormatter(console_formatter)
    
    logging.getLogger('').addHandler(console_handler)

    logging.info("Flask API startup")

    return app