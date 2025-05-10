from django.db import models
from users.models import CustomUser
from core.base_models import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    comment = models.ForeignKey('comments.Comment', on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post', 'comment')

    def __str__(self):
        return f"{self.user} liked {self.post or self.comment}"