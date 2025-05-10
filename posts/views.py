from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from .pagination import PostPagination
from posts.models import Like


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination

class LikePostView(APIView):
    def post(self, request, pk=None):
        try:
            post = Post.objects.get(id=pk)
            user = request.user
            like, created = Like.objects.get_or_create(post=post, user=user)

            if not created:
                return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)
        except Post.DoesNotExist:
            return Response({"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

class UnlikePostView(APIView):
    def post(self, request, pk=None):
        try:
            post = Post.objects.get(id=pk)
            user = request.user
            like = Like.objects.get(post=post, user=user)
            like.delete()  # Удаляем лайк
            return Response({"detail": "Post unliked successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({"detail": "You have not liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND)