from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer
from chat_tribe.permissions import IsPostOwnerOrReadOnly

class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsPostOwnerOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        post = get_object_or_404(self.queryset, pk=kwargs['pk'])
        serializer = self.get_serializer(post, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        # Associate the post update with the current user
        serializer.save(user=self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        post = self.get_object()
        self.check_object_permissions(request, post)  
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)