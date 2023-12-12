from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile

class Follower(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followed', on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'followed']

    def __str__(self):
        return f'{self.user} is following {self.followed}'