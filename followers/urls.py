from django.urls import path
from .views import FollowerList, FollowerDetail  # Import specific views

urlpatterns = [
    path('followers/', FollowerList.as_view(), name='follower-list-create'),
    path('followers/<int:pk>/', FollowerDetail.as_view(), name='follower-detail'),
]