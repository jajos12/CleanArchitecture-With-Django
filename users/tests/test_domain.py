from django.test import TestCase
from users.domain.models import User

class UserModelTest(TestCase):
    def test_set_password(self):
        user = User(username='testuser', email='test@example.com')
        user.set_password('password123')
        
        # Check that the password is hashed
        self.assertNotEqual(user.password, 'password123')
        self.assertTrue(user.check_password('password123'))  # Should return True
        self.assertFalse(user.check_password('wrongpassword'))  # Should return False