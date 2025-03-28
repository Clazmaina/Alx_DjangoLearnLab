from django.urls import path
from .views import UserCreate, UserLogin, UserProfile

urlpatterns = [
    path('register/', UserCreate.as_view(), name='user-register'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('profile/', UserProfile.as_view(), name='user-profile'),
]