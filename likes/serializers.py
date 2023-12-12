from rest_framework import serializers
from django.db import IntegrityError, transaction
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'created_at']

    def validate(self, data):
        # Ensure that a user can only like a post once
        post = data['post']
        user = self.context['request'].user  # Access the current user from the context

        try:
            with transaction.atomic():
                Like.objects.create(post=post, user=user)
        except IntegrityError:
            raise serializers.ValidationError("You have already liked this post.")

        return data