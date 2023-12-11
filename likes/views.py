from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Like
from .serializers import LikeSerializer

class LikeListView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

class LikeDetailView(generics.RetrieveAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
