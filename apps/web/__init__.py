from flask_restful import Api
from apps.web.resource import *
from flask import Blueprint

web_blue = Blueprint('web', __name__)
api_web = Api(web_blue)
api_web.add_resource(TaskAllApp, '/')