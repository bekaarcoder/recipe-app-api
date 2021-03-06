from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse("user:create")


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserAPITests(TestCase):
    # Tests the users API (public)

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        # Test creating user with valid payload is successful
        payload = {
            "email": "johndoe@gmail.com",
            "password": "Password123",
            "name": "John Doe",
        }
        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**response.data)
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", response.data)

    def test_user_exists(self):
        # Test creating a user that already exists
        payload = {"email": "johndoe@gmail.com", "password": "Password@123"}
        create_user(**payload)

        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        # Test password is more than 6 characters
        payload = {"email": "johndoe@gmail.com", "password": "Pass"}
        response = self.client.post(CREATE_USER_URL, payload)
        self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)
        user = get_user_model().objects.filter(email=payload["email"])
        user_exists = user.exists()
        self.assertFalse(user_exists)
