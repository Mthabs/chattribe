from django.urls import path
from .views import FriendListCreateView, FriendDetailView

urlpatterns = [
    path('friends/', FriendListCreateView.as_view(), name='friend-list-create'),
    path('friends/<int:pk>/', FriendDetailView.as_view(), name='friend-detail'),
   
]