from django.urls import path, include
# from users.api.views import UserView
from django.contrib import admin

urlpatterns = [
    path('api/users/', include('users.api.urls')),
    path('admin/', admin.site.urls),
]