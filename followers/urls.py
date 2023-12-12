from django.urls import path
from .views import FollowerListView, FollowerCreateView, FollowerDetailView

urlpatterns = [
    path('followers/', FollowerListView.as_view(), name='follower-list'),
    path('followers/create/', FollowerCreateView.as_view(), name='follower-create'),
    path('followers/<int:pk>/', FollowerDetailView.as_view(), name='follower-detail'),
]