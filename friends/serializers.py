from rest_framework import serializers
from .models import Friend
from django.contrib.auth.models import User

class FriendSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    friend_name = serializers.ReadOnlyField(source='friend.username')

    class Meta:
        model = Friend
        fields = ['id', 'user', 'created_at', 'friend', 'friend_name']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'error': 'Friendship already exists.'})