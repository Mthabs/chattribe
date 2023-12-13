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
        serializer.save(owner=self.request.user)

class FriendDetailView(generics.RetrieveDestroyAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [permissions.IsAuthenticated]
