from rest_framework import generics, permissions, serializers
from django.db import IntegrityError
from .models import Friend
from .serializers import FriendSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

class FriendListCreateView(generics.ListCreateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        friend = serializer.validated_data['friend']
        if Friend.objects.filter(user=user, friend=friend).exists():
            raise serializers.ValidationError({'error': 'Friendship already exists.'})
        serializer.save(user=user)

class FriendDetailView(generics.RetrieveDestroyAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        friend = self.get_object()
        if request.user == friend.user:
            return super().delete(request, *args, **kwargs)
        else:
            return Response({'detail': 'You do not have permission to delete this friend.'}, status=status.HTTP_403_FORBIDDEN)
