from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer

class ProfileList(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer