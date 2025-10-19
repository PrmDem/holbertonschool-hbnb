import unittest
from app import create_app
import json

class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid_email(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "kkhj",
            "last_name": "jjghg",
            "email": "invalid-email"
        })
        self.assertEqual(response.status_code, 400)

    def test_create_user_invalid_first_name(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "jjghg",
            "email": "aaa@gmail.com"
        })
        self.assertEqual(response.status_code, 400)

    def test_create_user_invalid_data_last_name(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "kkhj",
            "last_name": "",
            "email": "aaa@gmail.com"
        })
        self.assertEqual(response.status_code, 400)


    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        create_response = self.client.post('/api/v1/users/', json={
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com"
        })

        self.user_id = json.loads(create_response.data).get("id")

    def test_get_user_by_valid_id(self):
        response = self.client.get(f'/api/v1/users/{self.user_id}')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)
        self.assertIn("id", data)
        self.assertIn("first_name", data)
        self.assertIn("last_name", data)
        self.assertIn("email", data)
        self.assertEqual(data["id"], self.user_id)

    def test_get_user_by_invalid_id(self):
        invalid_id = "00000000-0000-0000-0000-000000000000"
        response = self.client.get(f'/api/v1/users/{invalid_id}')
        self.assertEqual(response.status_code, 404)

        data = json.loads(response.data)
        self.assertIn("error", data)

    def test_get_user_with_invalid_format_id(self):
        response = self.client.get('/api/v1/users/not-a-valid-uuid')
        self.assertIn(response.status_code, [400, 404])

