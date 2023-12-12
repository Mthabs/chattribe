from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    following_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'following_user']

    def __str__(self):
        return f"{self.user} follows {self.following_user} at {self.created_at}"