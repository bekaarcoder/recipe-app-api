from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = "johndoe@gmail.com"
        password = "Password@123"
        user = get_user_model().objects.create_user(
            email=email, password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        # test the email of the new user is normalized
        email = "johndoe@GMAIL.COM"
        password = "Password@123"
        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # Test user email for validation error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "Password@123")

    def test_create_new_superuser(self):
        # Test creating a new superuser
        user = get_user_model().objects.create_superuser(
            "superuser@gmail.com", "Password@123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
