from django.urls import path
from .views import LikeList, LikeDetail  # Import specific views

urlpatterns = [
    path('likes/', LikeList.as_view(), name='like-list'),
    path('likes/<int:pk>/', LikeDetail.as_view(), name='like-detail'),
]