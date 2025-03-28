from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, filters, generics, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from notifications.models import Notification
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)
        Notification.objects.create(
            recipient=comment.post.author,
            actor=self.request.user,
            verb='commented on your post',
            target=comment.post,
        )


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            raise ValidationError("Post does not exist.")

        try:
            like = serializer.save(user=self.request.user, post=post)
            Notification.objects.create(
                recipient=post.author,
                actor=self.request.user,
                verb='liked your post',
                target=post,
            )
        except Exception:
            raise ValidationError("You have already liked this post.")
        
class LikeDeleteView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, pk=post_id)
        like = get_object_or_404(Like, post=post, user=self.request.user)
        return like

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)