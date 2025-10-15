from app.models.base_model import BaseModel
from app.services import facade

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        try:
            if value != "":
                self.__text = value
        except Exception as e:
            return {"Error": f"{str(e)}"}, 404

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        try:
            if 0 < value < 6:
                self.__rating = value
        except Exception as e:
            return {"Value Error": f"{str(e)}"}, 404

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        try:
            place_value = facade.get_place(value.id)
            if place_value:
                self.__place = place_value
        except Exception as e:
            return {"Value Error": f"{str(e)}"}, 404

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        try:
            user_value = facade.get_user(value.id)
            if user_value:
                self.__user = user_value
        except Exception as e:
            return {"Error": f"{str(e)}"}, 404
