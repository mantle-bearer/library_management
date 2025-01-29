from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.throttling import UserRateThrottle
from .models import Book
from .serializers import BookSerializer

class BookThrottle(UserRateThrottle):
    rate = '100/min'

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    throttle_classes = [BookThrottle]

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    throttle_classes = [BookThrottle]
