from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        if value > datetime.date.today().year:
            raise
        serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    def create(self, validated_data):
        books_data = vaidated_data.pop('books',[])
        author = Author.objects.create(**validated_data)
        for book_data in books_data:
            Book.objects.create(author=author,**book_data)
            return author