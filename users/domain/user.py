from .models import User

class UserEntity:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def save(self):
        user = User(username=self.username, email=self.email)
        user.set_password(self.password)
        user.save()
        return user