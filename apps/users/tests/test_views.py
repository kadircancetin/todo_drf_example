from apps.core.test import BaseViewTestCase
from apps.users.tests.factories import UserFactory
from rest_framework import status


class TokenObtainPairViewTestCase(BaseViewTestCase):
    def setUp(self):
        self.anonym_client = self.get_anonymous_client()
        self.url = "/api/token/"

        self.example_password = "123"
        self.user = UserFactory(password=self.example_password)

        self.example_data = {
            "username": self.user.username,
            "password": self.example_password,
        }

    def test_login_and_get_token(self):
        response = self.anonym_client.post(self.url, data=self.example_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data.keys())
        self.assertIn("refresh", response.data.keys())

    def test_try_login_with_wrong_password(self):
        self.example_data['password'] += "wrong"
        response = self.anonym_client.post(self.url, data=self.example_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
