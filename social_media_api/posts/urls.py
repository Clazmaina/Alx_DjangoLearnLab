from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, LikeCreateView, LikeDeleteView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("feed/", FeedView.as_view(), name='feed'),
    path('posts/<int:post_id>/like/', LikeCreateView.as_view(), name='like-post'),
    path('posts/<int:post_id>/unlike/', LikeDeleteView.as_view(), name='unlike-post'),
]