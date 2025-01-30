from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book

class BookAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            'title': 'The Great Gatsby',
            'author': 'F. Scott Fitzgerald',
            'genre': 'Classic Fiction',
            'publication_date': '1925-04-10',
            'availability': 'available',
            'edition': '1st',
            'summary': 'A novel about the corruption of the American Dream.'
        }
        self.book = Book.objects.create(**self.book_data)
        self.book_url = reverse('book-retrieve-update-destroy', kwargs={'pk': self.book.pk})

    def test_create_book(self):
        response = self.client.post(reverse('book-list-create'), self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_books(self):
        response = self.client.get(reverse('book-list-create'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_book(self):
        response = self.client.get(self.book_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        updated_data = self.book_data.copy()
        updated_data['title'] = 'The Great Gatsby - Updated'
        response = self.client.put(self.book_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(self.book_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    

