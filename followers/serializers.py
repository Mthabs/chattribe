from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower
from django.contrib.auth.models import User

class FollowerSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    followed_name = serializers.ReadOnlyField(source='followed.user.username')

    class Meta:
        model = Follower
        fields = ['id', 'user', 'created_at', 'followed', 'followed_name']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'error': 'You have already liked this post.'})