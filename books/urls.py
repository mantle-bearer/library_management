from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/v1/books', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('api/v1/books/<int:id>', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-retrieve-update-destroy'),
]



