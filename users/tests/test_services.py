from django.test import TestCase
from users.services.user_service import UserService
from users.domain.models import User

class UserServiceTest(TestCase):
    def test_register_user(self):
        username = "testuser"
        email = "test@example.com"
        password = "password123"
        
        user = UserService.register_user(username, email, password)
        
        self.assertIsNotNone(user)
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_find_user(self):
        username = "testuser"
        email = "test@example.com"
        password = "password123"
        UserService.register_user(username, email, password)

        found_user = UserService.find_user(username)

        self.assertIsNotNone(found_user)
        self.assertEqual(found_user.username, username)
        self.assertEqual(found_user.email, email)