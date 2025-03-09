from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from .serializers import UserSerializer
from ..services.user_service import UserService
from ..domain.models import User

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = UserService.register_user(
            serializer.validated_data['username'],
            serializer.validated_data['email'],
            serializer.validated_data['password']
        )
        return user

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"

    def get(self, request, username):
        user = UserService.find_user(username)
        if user:
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)