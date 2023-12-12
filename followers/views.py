from rest_framework import generics, permissions
from .models import Follower
from .serializers import FollowerSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

class FollowerListCreateView(generics.ListCreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the user to the current authenticated user
        serializer.save(user=self.request.user)
        self.request.user.userprofile.following_id = serializer.instance.followed
        self.request.user.userprofile.save()

class FollowerDetailView(generics.RetrieveDestroyAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        # Override the delete method to check if the user requesting the delete is the owner
        follower = self.get_object()
        if request.user == follower.user:
            return super().delete(request, *args, **kwargs)
        else:
            return Response({'detail': 'You do not have permission to delete this follower.'}, status=status.HTTP_403_FORBIDDEN)

class FollowerListForUserView(generics.ListAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get the followers for the currently authenticated user
        return Follower.objects.filter(user=self.request.user)