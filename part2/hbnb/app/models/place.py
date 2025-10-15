from app.models.base_model import BaseModel
from app.services import facade


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner
        self.reviews = []
        self.amenities = []

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        try:
            if value and len(value) <= 100:
                self.__title = value
        except ValueError:
            return {"ValueError": "Title must be between 1 and 100 characters"}, 400

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        try:
            if isinstance(value, float) and value > 0:
                self.__price = value
        except ValueError:
            return {"ValueError": "Price must be a positive number"}, 400

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        try:
            if isinstance(value, float) and -90.00 <= value <= 90.00:
                self.__latitude = value
        except ValueError:
            return {"ValueError": "Latitude must be between -90.00 and 90.00"}, 400

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        try:
            if isinstance(value, float) and -180.00 <= value <= 180.00:
                self.__longitude = value
        except ValueError:
            return {"ValueError": "Longitude must be between -180.00 and 180.00"}, 400

    @property
    def owner_id(self):
        return self.__owner_id

    @owner_id.setter
    def owner_id(self, value):
        try:
            place_owner = facade.get_user(value.id)
            if place_owner:
                self.__owner_id = place_owner
        except Exception as e:
            return {"Error": f"{str(e)}"}, 400

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
