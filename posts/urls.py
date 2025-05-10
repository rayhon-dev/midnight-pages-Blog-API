from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:pk>/like', views.LikePostView.as_view(), name='like_post'),
    path('posts/<int:pk>/unlike', views.UnlikePostView.as_view(), name='unlike_post'),
]