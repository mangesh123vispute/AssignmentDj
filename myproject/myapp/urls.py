from django.urls import path
from .views import  ImageHashListView, ImageHashCreateView, ImageHashDetailView
urlpatterns = [
    path('image-hashes/', ImageHashListView.as_view(), name='imagehash-list'),
    path('image-hashes/create/', ImageHashCreateView.as_view(), name='imagehash-create'),
    path('image-hashes/<int:pk>/', ImageHashDetailView.as_view(), name='imagehash-detail'),
]
