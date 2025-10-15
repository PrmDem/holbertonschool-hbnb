from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Name of the place'),
    'description': fields.String(required=False, description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place location'),
    'longitude': fields.Float(required=True, description='Longitude of the place location'),
    'owner': fields.User(required=True, description='User who owns the place')
})

@api.route('/')
