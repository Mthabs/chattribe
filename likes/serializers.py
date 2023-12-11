from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate(self, data):
        # Ensure that a user can only like a post once
        post = data['post']
        user = data['user']
        if Like.objects.filter(post=post, user=user).exists():
            raise serializers.ValidationError("You have already liked this post.")
        return data