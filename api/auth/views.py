from flask import request
from flask_restx import Namespace, Resource, fields

auth_namespace = Namespace('auth', description='Authentication namespace')

@auth_namespace.route('/auth')
class Admin(Resource):

    def get(self):
        return {
            'message': 'Admin Login'
        }
    
class Student(Resource):
    def get(self):
        pass