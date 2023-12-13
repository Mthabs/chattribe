from rest_framework import serializers
from .models import UserProfile
from followers.models import Follower
from friends.models import Friend

class UserProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts = serializers.ReadOnlyField()
    followers = serializers.ReadOnlyField()
    following = serializers.ReadOnlyField()
    friends = serializers.ReadOnlyField()

    class Meta:
        model = UserProfile
        fields = ['id', 'owner', 'created_at', 'updated_at', 'bio', 'content', 'profile_picture', 'cover_photo', 'is_owner', 'following_id', 'posts','friends','followers','following']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        default_profile_picture_url = 'https://res.cloudinary.com/dnt7oro5y/image/upload/v1702078965/default_profile_yansvo.jpg'
        default_cover_photo_url = 'https://res.cloudinary.com/dnt7oro5y/image/upload/v1702078965/default_profile_ifketo.jpg'

        if not instance.profile_picture:
            representation['profile_picture'] = default_profile_picture_url

        if not instance.cover_photo:
            representation['cover_photo'] = default_cover_photo_url

        return representation

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.user

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

   # def get_friends(self, obj):
   #     request = self.context.get('request')
    #    if request.user.is_authenticated:
     #       friendships = Friend.objects.filter(user=request.user, friend=obj.user).first()
      #      return FriendSerializer(friendships).data if friendships else None
       # return None
        

   # def get_followers(self, obj):
    #    request = self.context.get('request')
     #   if request and request.user.is_authenticated:
      #      following = Follower.objects.filter(user=request.user, followed=obj.user).first()
       #     return FollowerSerializer(following).data if following else None
      #  return None