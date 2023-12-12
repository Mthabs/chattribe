class FriendSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    friend_name = serializers.ReadOnlyField(source='friend.username')

    class Meta:
        model = Friend
        fields = ['id', 'user', 'created_at', 'friend', 'friend_name']