from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Follower
from .serializers import FollowerSerializer

class FollowerListView(generics.ListAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Follower.objects.filter(Q(user=user) | Q(following_user=user))

class FollowerCreateView(generics.CreateAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FollowerDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Follower.objects.filter(Q(user=user) | Q(following_user=user))

    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            instance.delete()
        else:
            self.permission_denied(self.request)