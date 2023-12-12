from django.urls import path
from .views import FollowerListCreateView, FollowerDetailView, FollowerListForUserView

urlpatterns = [
    path('followers/', FollowerListCreateView.as_view(), name='follower-list-create'),
    path('followers/<int:pk>/', FollowerDetailView.as_view(), name='follower-detail'),
    path('followers/my-followers/', FollowerListForUserView.as_view(), name='follower-list-for-user'),
   
]