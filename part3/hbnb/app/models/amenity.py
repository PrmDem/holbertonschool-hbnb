from app.models.base_model import BaseModel
from sqlalchemy.orm import validates


class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

    @validates("name")
    def validate_name(self, key, value):
        if not value or len(value) > 50:
            raise ValueError("Name must be between 1 and 50 characters")
        return value
