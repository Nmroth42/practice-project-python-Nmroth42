import json

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class RegistrationTestCase(APITestCase):
    def test_post_action(self):
        """
        По POST-запросу на /api/users возвращается токен.
        """
        user_data = {'username':'username', 'password':'password'}

        response = self.client.post('/api/users/', user_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue("token" in json.loads(response.content))
