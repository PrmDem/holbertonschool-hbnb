from app.services.repositories.user_repo import UserRepository
from app.services.repositories.place_repo import PlaceRepository
from app.services.repositories.amenity_repo import AmenityRepository
from app.services.repositories.review_repo import ReviewRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()
        self.place_repo = PlaceRepository()
        self.review_repo = ReviewRepository()
        self.amenity_repo = AmenityRepository()

    # Method for user creation
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    # Retrieves a specific user from their id
    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    # Retrieves a specific user from their email
    def get_user_by_email(self, email):
        return self.user_repo.get_user_by_email(email)

    # Retrieves all users
    def all_users(self):
        return self.user_repo.get_all()

    # Updates some or all of a user's information
    def update_user(self, user_id, user_obj):
        return self.user_repo.update(user_id, user_obj)

    # Deletes a user
    def delete_user(self, user_id):
        return self.user_repo.delete(user_id)

    # Creates a new amenity, adds to repository
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    # Retrieves one amenity using its id
    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    # Retrieves all amenities
    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    # Updates an amenity
    def update_amenity(self, amenity_id, amenity_data):
        return self.amenity_repo.update(amenity_id, amenity_data)

    # Deletes an amenity
    def delete_amenity(self, amenity_id):
        return self.amenity_repo.delete(amenity_id)

    # Creates a new place, adds it to repo
    def create_place(self, place_data):
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    # Retrieves a place using its id
    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    # Retrieves all places
    def get_all_places(self):
        return self.place_repo.get_all()

    # Updates one or all of a place's info
    def update_place(self, place_id, place_data):
        return self.place_repo.update(place_id, place_data)

    # Deletes a place
    def delete_place(self, place_id):
        return self.place_repo.delete(place_id)

    # Creates a new review, adds it to repo
    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    # Retrieves a review by its id
    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    # Retrieves all reviews
    def get_all_reviews(self):
        return self.review_repo.get_all()

    # Retrieves all reviews written about a specific place
    def get_reviews_by_place(self, place_id):
        return self.review_repo.get_reviews_by_place(place_id)

    # Updates all or part of a review's info
    def update_review(self, review_id, review_data):
        return self.review_repo.update(review_id, review_data)

    # Deletes a review
    def delete_review(self, review_id):
        return self.review_repo.delete(review_id)

    # Checks whether a given user has already reviewed a given place
    def compare_review(self, user_id, place_id):
        reviews = self.review_repo.get_all()
        for review in reviews:
            if review.user_id == user_id and review.place_id == place_id:
                return True
        return False
