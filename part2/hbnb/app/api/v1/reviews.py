from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('reviews', description='Review operations')

# Define the review model for input validation and documentation
review_model = api.model('Review', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'user_id': fields.String(required=True, description='ID of the user'),
    'place_id': fields.String(required=True, description='ID of the place')
})

@api.route('/')
class ReviewList(Resource):
    @api.expect(review_model)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        review_data = api.payload
        new_review = facade.create_review(review_data)
        return {'id': new_review.id, 'text': new_review.text}, 201


    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews"""
        all_review = facade.get_all_reviews()
        reviews = [{
            "id": r.id,
            "text": r.text,
            "rating": r.rating,
            "user_id": r.user_id,
            "place_id": r.place_id
        } for r in all_review]
        return reviews, 200

@api.route('/<review_id>')
class ReviewResource(Resource):
    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review details by ID"""
        try:
            review = facade.get_review(review_id)
            return {
                "id": review.id,
                "text": review.text,
                "rating": review.rating,
                "user_id": review.user_id,
                "place_id": review.place_id
            }, 200
        except Exception as e:
            return {"error": f"Review not found: {str(e)}"}, 404

    @api.expect(review_model)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    def put(self, review_id):
        """Update a review's information"""
        try:
            review_put = facade.get_review(review_id)
            review_data = api.payload

            review_put.text = review_data.get('text', review_put.text)
            review_put.rating = review_data.get('rating', review_put.rating)
            review_put.user_id = review_data.get('user_id', review_put.user_id)
            review_put.place_id = review_data.get('place_id', review_put.place_id)
            return {"message": "Review updated successfully"}, 200
        except Exception as e:
            return {"error": f"Review not found: {str(e)}"}, 404

    @api.response(200, 'Review deleted successfully')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review"""
        try:
            review = facade.get_review(review_id)
            facade.delete_review(review_id)
            return {"message": "Review deleted successfully"}, 200
        except Exception as e:
            return {"error": f"Not Found: {str(e)}"}, 404

@api.route('/places/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place"""
        try:
            review = facade.get_reviews_by_place(place_id)
            reviews = [{
                "id": r.id,
                "text": r.text,
                "rating": r.rating,
                "user_id": r.user_id,
                "place_id": r.place_id
            } for r in review]
            return reviews, 200
        except Exception as e:
            return {"error": f"Review not found: {str(e)}"}, 404
