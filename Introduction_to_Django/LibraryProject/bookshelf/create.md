# Create a Book Instance

*Command:*
```python
>>> from bookshelf.models import Book
>>> book1 = Book(title="The Hitchhiker's Guide to the Galaxy", author="Douglas Adams", publication_year=1979)
>>> ["Book.objects.create", "George Orwell"]
>>> book1.save()
