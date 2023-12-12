from django.http import Http404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from chat_tribe.permissions import IsOwnerOrReadOnly

class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['is_owner'] = (
            self.request.user.is_authenticated and
            self.get_object().user == self.request.user
        )
        return context

    def retrieve(self, request, *args, **kwargs):
        comment = get_object_or_404(self.queryset, pk=kwargs['pk'])
        serializer = self.get_serializer(comment, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        self.check_object_permissions(request, comment)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
