from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from .models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    following_user = serializers.ReadOnlyField(source='following_user.username')

    class Meta:
        model = Follower
        fields = ['user', 'following_user', 'created_at']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        user = self.context['request'].user
        following_user_data = validated_data.get('following_user')
        following_user = User.objects.get(username=following_user_data['username'])
        try:
            follower_instance = Follower.objects.create(user=user, following_user=following_user)
        except IntegrityError:
            raise ValidationError("You are already following this user.")

        return follower_instance