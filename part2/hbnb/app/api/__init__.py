from flask_restx import Api
from app.api.v1.places import api as places_ns


api = Api(version='1.0', title='HBnB API', description='HBnB Application API')

   
api.add_namespace(places_ns, path='/api/v1/places')
