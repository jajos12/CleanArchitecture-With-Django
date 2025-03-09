from django.test import TestCase
from users.repositories.user_repository import UserRepository
from users.domain.models import User

class UserRepositoryTest(TestCase):
    def setUp(self):
        self.user = User(username='testuser', email='test@example.com')
        self.user.set_password('password123')
        self.user.save()

    def test_create_user(self):
        new_user = User(username='newuser', email='new@example.com')
        new_user.set_password('newpassword')
        UserRepository.create_user(new_user)

        self.assertIsNotNone(UserRepository.get_user_by_username('newuser'))

    def test_get_user_by_username(self):
        user = UserRepository.get_user_by_username('testuser')
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'testuser')

    def test_get_all_users(self):
        users = UserRepository.get_all_users()
        self.assertGreater(len(users), 0)  # Should return at least one user