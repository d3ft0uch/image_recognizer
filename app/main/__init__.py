from .config import config_by_name
from flask.app import Flask

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    return app
