from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'password': fields.String(required=True, description='Password of the user')
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new user"""
        user_data = api.payload

        # Simulate gitemail uniqueness check (to be replaced by real validation with persistence)
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
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
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200
    
    @api.expect(user_model, validate=True)
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def put(self, user_id):
        """
        update user
        """
        user_put = facade.get_user(user_id)
        if not user_put:
            return {'error': 'User not found'}, 404
        
        user_data = api.payload
        user_put.first_name = user_data.get('first_name', user_put.first_name)
        user_put.last_name = user_data.get('last_name', user_put.last_name)
        user_put.email = user_data.get('email', user_put.email)

        #problem pour save update, ajout dans facade de update_user etde la ligne en dessous mais plantage....
        # fonctionne sans sauvegarde juste return,voir avec priam gestion des classe user par exemple
        #facade.update_user(user_id, user_put)
        
        return {'id': user_put.id, 'first_name': user_put.first_name, 'last_name': user_put.last_name, 'email': user_put.email}, 200
