from sqlalchemy.orm import validates
from .base_model import BaseModel
from app.extensions import db
from app.services import facade

class Review(BaseModel):
    """Instantiates or updates Review information.

    Defines the following attributes:

    text (str), rating (int)
    place_id (str), user_id (str)

    Creation and update times, as well as UUID,
    are set via the call to BaseModel's init method.
    """

    __tablename__ = 'reviews'

    text = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    place_id = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String, nullable=False)

    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id

    @validates("text")
    def validate_text(self, key, value):
        if not value:
            raise ValueError("Text cannot be empty")
        return value

    @validates("rating")
    def validate_rating(self, key, value):
        if not (0 < value < 6):
            raise ValueError("Rating must be between 1 and 5")
        return value

    @validates("place")
    def validate_place(self, key, value):
        if not value:
            raise ValueError("Place ID cannot be empty")
        if (value not in val for val in facade.get_all_places()):
            raise ValueError(f"Place with ID {value} not found")
        return value

    @validates("user")
    def validate_user(self, key, value):
        if not value or value == "":
            raise ValueError("User ID cannot be empty")
        if (value not in val for val in facade.all_users()):
            raise ValueError(f"User with ID {value} not found")
        return value
