from ..domain.models import User

class UserRepository:
    @staticmethod
    def create_user(user):
        user.save()
        return user

    @staticmethod
    def get_user_by_username(username):
        return User.objects.filter(username=username).first()

    @staticmethod
    def get_all_users():
        return User.objects.all()