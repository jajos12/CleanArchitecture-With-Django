from ..repositories.user_repository import UserRepository
from ..domain.models import User

class UserUseCases:
    @staticmethod
    def register_user(username, email, password):
        user = User(username=username, email=email)
        user.set_password(password)
        return UserRepository.create_user(user)

    @staticmethod
    def find_user(username):
        return UserRepository.get_user_by_username(username)

    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()