from app.models.base_model import BaseModel
from sqlalchemy.orm import validates
from app.services import facade


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities=None, reviews=None):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = amenities if amenities is not None else []
        self.reviews = reviews if reviews is not None else []

    @validates("title")
    def validate_title(self, key, value):
        if not value or len(value) > 100:
            raise ValueError("Title must be between 1 and 100 characters")
        return value

    @validates("price")
    def validate_price(self, key, value):
        if not isinstance(value, float) or value < 0:
            raise ValueError("Price must be a positive number")
        return value

    @validates("latitude")
    def validate_latitude(self, key, value):
        if not isinstance(value, float) or -90.00 > value < 90.00:
            raise ValueError("Latitude must be between -90.00 and 90.00")
        return value

    @validates("longitude")
    def validate_longitude(self, key, value):
        if not isinstance(value, float) or -180.00 > value < 180.00:
            raise ValueError("Longitude must be between -180.00 and 180.00")
        return value

    @validates("owner_id")
    def validate_owner_id(self, key, value):
        if (value not in all.id for all in facade.all_users()):
            raise ValueError("Invalid user ID")
        return value

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
