from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView
# from django.conf.urls import handler404


urlpatterns = [
    path('api/v1/books', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('api/v1/books/<int:pk>', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-retrieve-update-destroy'),
    
]

