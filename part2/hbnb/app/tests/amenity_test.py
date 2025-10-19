import unittest
from app import create_app


class TestPlaceEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_amenity_creation(self): #basic amenity creation
        response = self.client.post('/api/v1/amenities/', json={
            "name": "swimming pool"
        })
        self.assertEqual(response.status_code, 201)

    def test_amenity_no_input(self): # no valid name input
        response = self.client.post('/api/v1/amenities/', json={
            "name": 123
        })
        self.assertEqual(response.status_code, 400)

    def test_find_amenity_by_id(self): # finding amenity by appending id to endpoint
        response = self.client.post('/api/v1/amenities/', json={
            "name": "roomba"
        })
        amenity_data = response.get_json()
        amenity_id = amenity_data["id"]
        new_response = self.client.get(f'/api/v1/amenities/{amenity_id}')
        self.assertEqual(new_response, 200)
