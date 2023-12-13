from django.db.models import Count
from rest_framework import generics, filters
from chat_tribe.permissions import IsOwnerOrReadOnly
from .models import UserProfile
from .serializers import UserProfileSerializer


class ProfileList(generics.ListAPIView):
    queryset = UserProfile.objects.annotate(
        posts=Count('owner__post', distinct=True),
        followers=Count('owner__followed', distinct=True),
        following=Count('owner__following', distinct=True),
        friends=Count('owner__friend', distinct=True)
    ).order_by('-created_at')
    serializer_class = UserProfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'posts',
        'followers',
        'following',
        'friends',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = UserProfile.objects.annotate(
        posts=Count('owner__post', distinct=True),
        followers=Count('owner__followed', distinct=True),
        following=Count('owner__following', distinct=True),
        friends=Count('owner__friend', distinct=True)
    ).order_by('-created_at')
    serializer_class = UserProfileSerializer

   # def retrieve(self, request, *args, **kwargs):
    #    profile = get_object_or_404(UserProfile, pk=kwargs['pk'])
    #    serializer = self.get_serializer(profile, context={'request': request})
    #    return Response(serializer.data, status=status.HTTP_200_OK)

    #def update(self, request, *args, **kwargs):
     #   profile = self.get_object()
     #   serializer = self.get_serializer(profile, data=request.data, context={'request': request})
     #   if serializer.is_valid():
      #      serializer.save()
      #      return Response(serializer.data, status=status.HTTP_200_OK)
      #  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from .views import ProfileList, ProfileDetail