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
    'description': fields.String(required=False, description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's"),
    'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Create a new place"""
        current_user = get_jwt_identity()
        try:
            place_data = api.payload

            required = ['title', 'price', 'latitude', 'longitude', 'owner_id', 'description']
            for r in required:
                if r not in place_data or place_data[r] in [None, ""]:
                    return {"error": f"'{r}' field is required and cannot be empty"}, 400

            new_place = facade.create_place(place_data)
            return {
                    'id': new_place.id,
                    'title': new_place.title,
                    'description': new_place.description,
                    'price': new_place.price,
                    'latitude': new_place.latitude,
                    'longitude': new_place.longitude,
                    'owner_id': new_place.owner_id
                }, 201
        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}, 400


    @api.response(200, 'List of places retrieved successfully')
    @api.response(404, 'Places not found')
    def get(self):
        """Retrieve a list of all places"""
        try:
            places = facade.get_all_places()
            if not places:
                return {"error": "No places found"}, 404
            all_places = [{
                'id': place.id,
                'title': place.title,
                'latitude': place.latitude,
                'longitude': place.longitude,
            } for place in places]
            return all_places, 200
        except Exception as e:
            return {"Error": str(e)}, 404


@api.route('/<place_id>')
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
        
            amenities_data = []
            amenity_ids = place.amenities if place.amenities else []
            
            for amenity_id in amenity_ids: 
                a = facade.get_amenity(amenity_id)
                if a:
                    amenities_data.append({"id": a.id, "name": a.name})

            reviews_data = []
            review_ids = place.reviews if place.reviews else []
            
            for review_id in review_ids: 
                r = facade.get_review(review_id)
                if r:
                    reviews_data.append({
                        "id": r.id,
                        "text": r.text,
                        "rating": r.rating,
                        "user_id": r.user_id,
                        "place_id": r.place_id
                    })
            
            return {
                "id": place.id,
                "title": place.title,
                "description": place.description,
                "latitude": place.latitude,
                "longitude": place.longitude,
                "owner": owner_data,
                "amenities": amenities_data,
                "reviews": reviews_data
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
        try:
            place = facade.get_place(place_id)
        except Exception as e:
            return {'error': str(e)}, 404

        # Checks whether action is permitted for the user
        user_id = current_user.get('id')
        if not current_user.get('is_admin') and place.owner_id != user_id:
            return {'error': 'Unauthorized action'}, 403

        try:
            place_data = api.payload
            facade.update_place(place_id, place_data)
            return {"message": "Place updated successfully"}, 200
        except ValueError:
            return {"ValueError": "Invalid input data"}, 400
        except Exception as e:
            return {"Error": str(e)}, 404


    @api.response(200, 'Place deleted successfully')
    @api.response(404, 'Place not found')
    @jwt_required()
    def delete_place(place_id):
        """deletes a place if user is authorised"""
        current_user = get_jwt()
        current_place = facade.get_place(place_id)

        if not current_place:
            return {'error': 'Place not found'}, 404
        if not current_user['is_admin'] or current_user['id'] != current_place.owner_id:
            return {'error': 'Unauthorized action'}, 403

        try:
            facade.delete_place(place_id)
            return {'message': 'Place deleted successfully'}, 200
        except Exception as e:
            return {'error': str(e)}
