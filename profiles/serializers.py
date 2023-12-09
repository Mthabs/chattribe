from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserProfile
        fields = ['user_id', 'user', 'created_at', 'updated_at', 'bio', 'content', 'profile_picture', 'cover_photo']