from django.urls import path
from .views import CommentList, CommentDetail  # Import specific views

urlpatterns = [
    path('comments/', CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
]