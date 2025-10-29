from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')
api = Namespace('admin', description='Admin operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user'),
    'is_admin': fields.String(required=True, description='Permission level of the user')
})

@api.route('/')
class UserCreate(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        user_data = api.payload
        email = user_data.get('email')

        # Check if email is already in use
        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400

        try:
            new_user = facade.create_user(user_data)
        except:
            return {'error': 'invalid input data'}, 400

        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201

@api.route('/admin')
class AdminUserCreate(Resource):
    """Class and endpoint used to create as Admin
    As opposed to regular / from where users can be
    created by non-admin;

    This is to test our endpoints more easily
    """
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        current_user = get_jwt()
        if not current_user.get('is_admin'):
           return {'error': 'Admin privileges required'}, 403

        user_data = api.payload
        email = user_data.get('email')

        # Check if email is already in use
        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400

        try:
            new_user = facade.create_user(user_data)
        except:
            return {'error': 'invalid input data'}, 400

        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201
    
    @api.response(200, 'list of user')
    @api.response(500, 'Internal server error')
    def get(self):
        """
        retrieved all users
        """
        try:
            user_all = facade.all_users()
            user_list = []
            for user in user_all:
                user_list.append({
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
                })
            return user_list, 200
        except Exception as e:
            return {"error": f"error user list: {str(e)}"}, 500
    
@api.route('/<user_id>')
class AdminUserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200


    @api.expect(user_model)
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    @jwt_required()
    def put(self, user_id):
        """
        update user after verifying autorisations
        """
        current_user = get_jwt()
        
        # If 'is_admin' is part of the identity payload
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        user_data = api.payload
        email = user_data.get('email')

        if email:
            # Check if email is already in use
            old_user = facade.get_user_by_email(email)
            if old_user and old_user.id != user_id:
                return {'error': 'Email is already in use'}, 400

        existing_user = facade.get_user(user_id)
        if not existing_user:
            return {'error': 'User not found'}, 404
        
        user_data = api.payload

        if 'email' in user_data or 'password' in user_data:
            return {'error': 'You cannot modify email or password.'}, 400
        
        try:
            existing_user.first_name = user_data.get('first_name', existing_user.first_name)
        except ValueError as e:
            return {'error': str(e)}, 400
        try:
            existing_user.last_name = user_data.get('last_name', existing_user.last_name)
        except ValueError as e:
            return {'error': str(e)}, 400
        try:
            existing_user.email = user_data.get('email', existing_user.email)
        except ValueError as e:
            return {'error': str(e)}, 400
        try:
            existing_user.password = user_data.get('password', existing_user.password)
        except ValueError as e:
            return {'error': str(e)}, 400

        facade.update_user(user_id, {
            'first_name': existing_user.first_name,
            'last_name': existing_user.last_name
        })

        # problem pour save update, ajout dans facade de update_user et de la ligne en dessous mais plantage....
        # fonctionne sans sauvegarde juste return,voir avec priam gestion des classe user par exemple
        # facade.update_user(user_id, user_put)
        
        return {'id': existing_user.id, 'first_name': existing_user.first_name, 'last_name': existing_user.last_name, 'email': existing_user.email}, 200
