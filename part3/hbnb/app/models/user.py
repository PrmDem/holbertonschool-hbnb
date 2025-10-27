from app.models.base_model import BaseModel
from app.extensions import bcrypt
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
# correct format to verify user email against


class User(BaseModel):
    """Instantiates or updates user information.

    Defines the following user attributes:
    first_name (str), last_name (str), email (str)
    is_admin (bool), places (list)

    Creation and update times, as well as UUID,
    are set via the call to BaseModel's init method.

    """
    def __init__(self, first_name, last_name, email, password, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = self.hash_password(password)
        self.is_admin = is_admin
        self.places = []

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if 0 < len(value) <= 50:
            self.__first_name = value
        else:
            raise ValueError("First name must be between 1 and 50 characters")

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if 0 < len(value) <= 50:
            self.__last_name = value
        else:
            raise ValueError("Last name must be between 1 and 50 characters")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("Email can t be empty")
        if not re.fullmatch(regex, value):
            raise ValueError("Invalid email format")
        self.__email = value

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        return self.password

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)

    def owned_places(self, place):
        """Add an owned place to the user"""
        self.places.append(place)
