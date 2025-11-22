from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'picture': fields.String(description='Picture of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'location': fields.String(description='Continent on which the place is located'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's"),
    'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
})

@api.route('/', strict_slashes=False)
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Create a new place"""
        current_user = get_jwt()
        if not current_user.get('is_admin'):
           return {'error': 'Admin privileges required'}, 403

        try:
            place_data = api.payload

            required = ['title', 'price', 'latitude', 'longitude', 'owner_id']
            for r in required:
                if r not in place_data or place_data[r] in [None, ""]:
                    return {"error": f"'{r}' field is required and cannot be empty"}, 400

            new_place = facade.create_place(place_data)
            return {
                    'id': new_place.id,
                    'title': new_place.title,
                    'picture': new_place.picture,
                    'description': new_place.description,
                    'price': new_place.price,
                    'latitude': new_place.latitude,
                    'longitude': new_place.longitude,
                    'location': new_place.location,
                    'owner_id': new_place.owner_id
                }, 201
        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}, 400

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        try:
            places = facade.get_all_places()
            if not places:
                return {"error": "No places found"}, 404
            all_places = [{
                'id': place.id,
                'title': place.title,
                'picture': place.picture,
                'description': place.description,
                'price': place.price,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'location': place.location
            } for place in places]
            return all_places, 200
        except Exception as e:
            return {"Error": f"{str(e)}"}, 404

@api.route('/<place_id>', strict_slashes=False)
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        try:
            place = facade.get_place(place_id)
            if not place:
                return {"error": "Place not found"}, 404
            
            owner = facade.get_user(place.owner_id)

            if owner:
                owner_data = {
                    "id": owner.id,
                    "first_name": owner.first_name,
                    "last_name": owner.last_name,
                    "email": owner.email
                }
            else:
                owner_data = None
        
            amenities = place.amenities
            reviews = place.reviews
            
            return {
                "id": place.id,
                "title": place.title,
                "picture": place.picture,
                "description": place.description,
                "price": place.price,
                "latitude": place.latitude,
                "longitude": place.longitude,
                "location": place.location,
                "owner": owner_data,
                "amenities": [
                    {"id": a.id,
                    "name": a.name}
                    for a in amenities
                ],
                "reviews": [
                    {
                        "id": r.id,
                        "text": r.text,
                        "rating": r.rating,
                        "user": {
                            "id": r.user.id,
                            "first_name": r.user.first_name,
                            "last_name": r.user.last_name
                        }
                    } for r in reviews]
            }, 200
        
        except Exception as e:
            return {"Error": f"{str(e)}"}, 404

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, place_id):
        """Update a place's information"""
        current_user = get_jwt()

        # Set is_admin default to False if not exists
        is_admin = current_user.get('is_admin', False)
        user_id = get_jwt_identity()

        place = facade.get_place(place_id)
        if not is_admin and place.owner_id != user_id:
            return {'error': 'Unauthorized action'}, 403

        try:
            place_put = facade.get_place(place_id)
            if not place_put:
                return {"error": "Place not found"}, 404
            if not is_admin and place_put.owner_id != current_user:
                return {'error': 'Unauthorized action'}, 403
            
            required = ['title', 'price', 'description']
                    
            place_data = api.payload

            for r in required:
                if r not in place_data or place_data[r] in [None, ""]:
                    return {"error": f"'{r}' field is required and cannot be empty"}, 400
                    
            if place_data["price"] <= 0:
                return {"error": "Price must be greater than 0"}, 400
                    
            if not isinstance(place_data, dict):
                return {"error": "Invalid input data format"}, 400
            
            place_put.title = place_data.get('title', place_put.title)
            place_put.picture = place_data.get('picture', place_put.picture)
            place_put.description = place_data.get('description', place_put.description)
            place_put.price = place_data.get('price', place_put.price)
            place_put.latitude = place_data.get('latitude', place_put.latitude)
            place_put.longitude = place_data.get('longitude', place_put.longitude)
            place_put.location = place_data.get('location', place_put.location)
            place_put.owner_id = place_data.get('owner_id', place_put.owner_id)
            place_put.amenities = place_data.get('amenities', place_put.amenities)
            place_put.reviews = place_data.get('reviews', place_put.reviews)
            return {"message": "Place updated successfully"}, 200
        except ValueError:
            return {"ValueError": "Invalid input data"}, 400
        except Exception as e:
            return {"Error": f"{str(e)}"}, 404
