from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['post', 'user']  

    def __str__(self):
        return f"Like by {self.user} on Post {self.post} at {self.created_at}"
