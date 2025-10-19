from app.models.base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, v_name):
        try:
            if v_name and len(v_name) <= 50:
                self.__name = v_name
        except ValueError:
            return {"ValueError": "Name must be between 1 and 50 characters"}, 400
