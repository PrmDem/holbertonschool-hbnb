from app.persistence.repository import SQLAlchemyRepository
from app.models.place import Place
from app import db


class PlaceRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Place)

    def get_user_by_email(self, email):
        return self.model.query.filter_by(email=email).first()
