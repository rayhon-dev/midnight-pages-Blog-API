from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'comments', views.CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('comments/<int:pk>/like/', views.LikeCommentView.as_view(), name='like_comment'),
    path('comments/<int:pk>/unlike/', views.UnlikeCommentView.as_view(), name='unlike_comment'),
]