from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer
from rest_framework.throttling import UserRateThrottle
from django.http import Http404
from django.core.cache import cache
from datetime import datetime, timedelta

class BookThrottle(UserRateThrottle):
    rate = '100/min'
    scope = 'book-throttle'

    def get_cache_key(self, request, view):
        ident = self.get_ident(request)
        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }

    def get_history(self, request):
        cache_key = self.get_cache_key(request, None)
        return cache.get(cache_key, [])

    def get_rate_limit_headers(self, request):
        cache_key = self.get_cache_key(request, None)
        history = cache.get(cache_key, [])
        now = self.timer()
        while history and history[-1] <= now - self.duration:
            history.pop()
        remaining = self.num_requests - len(history)
        reset_time = (history[0] + self.duration - now) if history else self.duration
        return {
            "X-RateLimit-Limit": str(self.num_requests),
            "X-RateLimit-Remaining": str(max(remaining, 0)),
            "X-RateLimit-Reset": str(int(now + reset_time))
        }

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    throttle_classes = [BookThrottle]

    def post(self, request, *args, **kwargs):
        try:
            self.check_throttles(request)
            throttle_headers = self.get_throttles()[0].get_rate_limit_headers(request)
            response = self.create(request, *args, **kwargs)
            response_data = response.data
            response_data["status"] = "success"
            response_data["message"] = "Book created successfully."
            response_data["headers"] = throttle_headers
            return Response(response_data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    throttle_classes = [BookThrottle]
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        try:
            self.check_throttles(request)
            throttle_headers = self.get_throttles()[0].get_rate_limit_headers(request)
            response = self.retrieve(request, *args, **kwargs)
            response_data = response.data
            response_data["status"] = "success"
            response_data["message"] = "Book details retrieved successfully."
            response_data["headers"] = throttle_headers
            return Response(response_data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            raise Http404
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, *args, **kwargs):
        try:
            self.check_throttles(request)
            throttle_headers = self.get_throttles()[0].get_rate_limit_headers(request)
            response = self.update(request, *args, **kwargs)
            response_data = response.data
            response_data["status"] = "success"
            response_data["message"] = "Book details updated successfully."
            response_data["headers"] = throttle_headers
            return Response(response_data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            raise Http404
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        try:
            self.check_throttles(request)
            throttle_headers = self.get_throttles()[0].get_rate_limit_headers(request)
            response = self.destroy(request, *args, **kwargs)
            response_data = {
                "status": "success",
                "message": "Book deleted successfully.",
                "headers": throttle_headers
            }
            return Response(response_data, status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            raise Http404
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
