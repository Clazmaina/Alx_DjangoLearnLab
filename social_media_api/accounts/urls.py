from django.urls import path
from .views import UserCreate, UserLogin, UserProfile, FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', UserCreate.as_view(), name='user-register'),
    path('login/', UserLogin.as_view(), name='user-login'),
    path('profile/', UserProfile.as_view(), name='user-profile'),
    path('follow/<int:pk>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:pk>/', UnfollowUserView.as_view(), name='unfollow-user'),
]