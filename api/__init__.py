from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(app)

# Path: SchoolifyAPI\api\__init__.py
from . import api

# Path: SchoolifyAPI\api\api.py
from . import api

ns = api.namespace('school', description='School API')
