from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('admin', description='Admin operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user'),
    'is_admin': fields.Boolean(required=True, description='Permission level of the user')
})

@api.route('/', strict_slashes=False)
class AdminUserCreate(Resource):
    """Class and endpoint used to create a user
    Only administrators have authorisation
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
        except Exception as e:
            return {'error': str(e)}, 400

        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201

    @api.response(200, 'list of users')
    @api.response(500, 'Internal server error')
    def get(self):
        """
        retrieves all users
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


@api.route('/<user_id>', strict_slashes=False)
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
        """update user after verifying autorisations"""
        current_user = get_jwt()
        
        # If 'is_admin' is part of the identity payload
        is_admin = current_user.get('is_admin', False)
        # If the user is modifying their own profile
        is_owner = (get_jwt_identity() == user_id)
        
        # Refuses input from unauthorised users
        if not (is_admin or is_owner):
            return {'error': 'Unauthorised action'}, 403

        # Gets the user's profile information
        user_put = facade.get_user(user_id)
        if not user_put:
            return {'error': 'User not found'}, 404
        
        # Get the incoming information
        user_data = api.payload

        # Ensures email and password can't be changed by anyone other than the user
        if ((current_user.get('id') != user_id) and (
                (user_data.email != user_put.email) or 
                (user_data.password != user_put.password)
            )):
            return {'error': 'You cannot modify email or password'}, 400

        # updates user info
        try:
            facade.update_user(user_id, user_data)
        except:
            return {'error': 'invalid input data'}, 400

        return {'id': user_put.id, 'first_name': user_put.first_name, 'last_name': user_put.last_name, 'email': user_put.email}, 200
