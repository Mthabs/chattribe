from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='id')
    user = serializers.ReadOnlyField(source='user.username')
    profile_id = serializers.ReadOnlyField(source='user.userprofile.id')
    profile_picture = serializers.ReadOnlyField(source='user.userprofile.profile_picture.url')
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'user_id', 'profile_id', 'user', 'content', 'post_picture', 'header', 'created_at', 'updated_at', 'is_owner', 'profile_picture']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        default_post_picture_url = 'https://res.cloudinary.com/dnt7oro5y/image/upload/v1702078965/default_post_wv7bvz.jpg'
        
        if not instance.post_picture:
            representation['post_picture'] = default_post_picture_url

        return representation

    def validate_post_picture(self, value):
        # Add your image size validation logic here
        max_size = 2 * 1024 * 1024  # 2 MB
        if value.size > max_size:
            raise serializers.ValidationError('Image size cannot exceed 2 MB.')
        if value.height > 4096:
            raise serializers.ValidationError('Image height cannot exceed 4096px.')
        if value.width > 4096:
            raise serializers.ValidationError('Image width cannot exceed 4096px.')
        return value

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.user