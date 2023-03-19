from flask import request
from flask_restx import Namespace, Resource, fields

auth_namespace = Namespace('auth', description='Authentication namespace')

signup_model = auth_namespace.model('Auth', {
    'id': fields.Integer(readonly=True, description='The unique identifier of a user'),
    'name': fields.String(required=True, description='Name'),
    'email': fields.String(required=True, description='Email'),
    'username': fields.String(required=True, description='Username'),
    'password': fields.String(required=True, description='Password')
})

@auth_namespace.route('/auth')
class Admin(Resource):

    def get(self):
        return {
            'message': 'Admin Login'
        }
    
class Student(Resource):
    def get(self):
        pass