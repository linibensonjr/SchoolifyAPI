from flask import Flask
from flask_restx import Api
from .config.config import config_dict
from .students.views import students_namespace
from .auth.views import auth_namespace


def create_app(config=config_dict['dev']):
    app = Flask(__name__)
    api = Api(app)

    app.config.from_object(config)

    api.add_namespace(auth_namespace)
    api.add_namespace(students_namespace)
 

    return app
