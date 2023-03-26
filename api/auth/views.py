from flask import request
from flask_restx import Namespace, Resource, fields
from werkzeug.security import generate_password_hash
from ..models.users import User
from http import HTTPStatus
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required

auth_namespace = Namespace('auth', description='Authentication namespace')

signup_model = auth_namespace.model(
    'SignUp', {
    'id': fields.Integer(readonly=True, description='The unique identifier of a user'),
    'name': fields.String(required=True, description='Name'),
    'email': fields.String(required=True, description='Email'),
    'username': fields.String(required=True, description='Username'),
    'password': fields.String(required=True, description='Password')
})

user_model = auth_namespace.model(
    'User', {
        'id': fields.Integer(),
        'name': fields.String(required=True, description="A name"),
        'username': fields.String(required=True, description="A username"),
        'email': fields.String(required=True, description="An email"),
        'password_hash': fields.String(required=True, description='A password'),
        'is_active': fields.Boolean(description="This shows that User is active or not"),
        'is_staff': fields.Boolean(description="This shows that User is a staff or not")
    }
)

login_model = auth_namespace.model(
    'Login', {
        'email': fields.String(required=True, description="An email"),
        'password': fields.String(required=True, description='A password')
    }
)

@auth_namespace.route('/signup')
class Admin(Resource):
    @auth_namespace.expect(signup_model)
    @auth_namespace.marshal_with(user_model)
    def post(self):
        data = request.get_json()
        name = data.get('name')
        username = data.get('username')
        email = data.get('email')
        password_hash = generate_password_hash(data.get('password'))

        user = User(name=name, username=username, email=email, password=password_hash)
        user.save()

        return user, HTTPStatus.CREATED
    
@auth_namespace.route('/login')
class Login(Resource):
        @auth_namespace.expect(login_model)
        def post(self):
            '''Login a user'''
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')

            user = User.query.filter_by(email=email).first()

            if user and check_password_hash(user.password, password):
                access_token = create_access_token(identity=user.username)
                refresh_token = create_refresh_token(identity=user.username)

                response = {
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }

                return response, HTTPStatus.CREATED
            
            return {'message': 'login failed'}, HTTPStatus.UNAUTHORIZED

    
@auth_namespace.route('/refresh')
class Refresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        email = get_jwt_identity()
        return {'username': email}, HTTPStatus.OK