from flask_restx import Api
from flask import Blueprint

from .main.controller.app_controller import api as app_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='Image scanner',
    version='0.0.1',
)

api.add_namespace(app_ns, path="")
