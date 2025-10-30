from app.services import facade
from sqlalchemy.orm import validates
from .base_model import BaseModel
from app.extensions import bcrypt, db
import uuid


class Place(BaseModel):
    """Instantiates or updates Place information.

    Defines the following attributes:
    title (str), description (str), owner_id (str)
    price (float), latitude (float), longitude (float)
    amenities (list), reviews (list)

    Creation and update times, as well as UUID,
    are set via the call to BaseModel's init method.

    """
    __tablename__ = 'users'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String, nullable=False)
    amenities = db.Column(db.List, nullable=True)
    reviews = db.Column(db.List, nullable=True)

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

    @validates("reviews")
    def validate_add_review(self, key, review):
        """Add a review to the place."""
        if (review not in all.id for all in facade.get_all_reviews()):
            raise ValueError("Invalid review ID")
        self.reviews.append(review)
        return self.reviews

    @validates("amenities")
    def validate_add_amenitiy(self, key, amenity):
        """Add a review to the place."""
        if (amenity not in all.id for all in facade.get_all_amenities()):
            raise ValueError("Invalid amenity ID")
        self.amenities.append(amenity)
        return self.amenities
    