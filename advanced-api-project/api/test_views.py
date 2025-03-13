from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book, Author
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class BookCRUDTests(APITestCase):
    def setUp(self):
        # Create an author
        self.author = Author.objects.create(name="Test Author")
        # Create a book
        self.book = Book.objects.create(title="Test Book", author=self.author, publication_year=2023)
        # Create a user
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        # Create a token for the user
        self.token = Token.objects.create(user=self.user)
        # Authenticate the client with the token
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_book(self):
        url = reverse('book-list')
        data = {"title": "New Book", "author": self.author.id, "publication_year": 2024}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  
       