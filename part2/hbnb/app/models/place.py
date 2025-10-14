from app.models.base_model import BaseModel


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if value and len(value) <= 100:
            self.__title = value
        else:
            raise ValueError("Title must be between 1 and 100 characters")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if isinstance(value, float) and value > 0:
            self.__price = value
        else:
            raise ValueError("Price must be a positive number")

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        if isinstance(value, float) and -90.00 <= value <= 90.00:
            self.__latitude = value
        else:
            raise ValueError("Latitude must be between -90.00 and 90.00")

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        if isinstance(value, float) and -180.00 <= value <= 180.00:
            self.__longitude = value
        else:
            raise ValueError("Longitude must be between -180.00 and 180.00")

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # check w/ persistence model for user ?
        self.__owner = value

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)
