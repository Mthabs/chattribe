from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Friend
from .serializers import FriendSerializer

class FriendListCreateView(generics.ListCreateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

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
