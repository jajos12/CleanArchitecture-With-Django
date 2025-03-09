from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class UserAPITest(APITestCase):
    def test_create_user(self):
        url = reverse('user-list-create')
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_user(self):
        self.client.post(reverse('user-list-create'), {'username': 'testuser', 'email': 'test@example.com', 'password': 'password123'}, format='json')
        response = self.client.get(reverse('user-detail', args=['testuser']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_not_found(self):
        response = self.client.get(reverse('user-detail', args=['nonexistentuser']))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)