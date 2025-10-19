from app.models.base_model import BaseModel
from app.services import facade

class Review(BaseModel):
    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        if not value:
            raise ValueError("Text cannot be empty")
        self.__text = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if not (0 < value < 6):
            raise ValueError("Rating must be between 1 and 5")
        self.__rating = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        if not value:
            raise ValueError("Place ID cannot be empty")
        place_value = facade.get_place(value)
        if not place_value:
            raise ValueError(f"Place with ID {value} not found")
        self.__place = place_value

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        if not value or value == "":
            raise ValueError("User ID cannot be empty")
        user_value = facade.get_user(value)
        if not user_value:
            raise ValueError(f"User with ID {value} not found")
        self.__user = user_value
