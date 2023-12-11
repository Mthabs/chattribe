from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Like
from .serializers import LikeSerializer
from chat_tribe.permissions import IsOwnerOrReadOnly

class LikeListView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        try:
            with transaction.atomic():
                serializer.is_valid(raise_exception=True)
                serializer.save(user=request.user)
        except IntegrityError:
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LikeDetailView(generics.RetrieveDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        like = get_object_or_404(self.queryset, pk=kwargs['pk'])
        serializer = self.get_serializer(like, context={'request': request})
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        like = self.get_object()
        self.check_object_permissions(request, like)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
