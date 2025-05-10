from rest_framework import serializers
from users.serializers import CustomUserSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'is_active', 'created_at', 'updated_at', 'comments_count', 'likes_count')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_likes_count(self, obj):
        return obj.likes.count()

    def create(self, validated_data):
        user = self.context['request'].user
        return Post.objects.create(user=user, **validated_data)
