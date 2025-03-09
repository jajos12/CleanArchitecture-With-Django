from django.core.management.base import BaseCommand
from users.domain.models import User

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        users = [
            {'username': f'testuser{i}', 'email': f'testuser{i}@example.com', 'password': 'password123'}
            for i in range(1, 21)  # Generates 20 users
        ]

        for user_data in users:
            user = User(
                username=user_data['username'],
                email=user_data['email'],
            )
            user.set_password(user_data['password'])  # Hash the password
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created user {user.username}'))