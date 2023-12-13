from django.urls import path
from .views import PostListView, PostDetailView  # Import specific views

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]