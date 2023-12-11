from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    profile_id = serializers.ReadOnlyField(source='user.userprofile.id')
    profile_picture = serializers.ReadOnlyField(source='user.userprofile.profile_picture_url')
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'profile_id', 'user', 'post', 'content', 'created_at', 'updated_at', 'profile_picture', 'is_owner']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        default_profile_picture_url = 'https://res.cloudinary.com/dnt7oro5y/image/upload/v1702078965/default_profile_yansvo.jpg'
        
        if 'profile_picture' not in representation:
            representation['profile_picture'] = default_profile_picture_url
      
        return representation

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.user