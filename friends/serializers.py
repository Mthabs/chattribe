from rest_framework import serializers
from .models import Friend

class FriendSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    friend_name = serializers.ReadOnlyField(source='friend.username')

    class Meta:
        model = Friend
        fields = ['id', 'owner', 'created_at', 'friend', 'friend_name']