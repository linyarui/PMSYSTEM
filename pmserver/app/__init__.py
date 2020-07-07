from flask import Flask
from exts import db
import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


