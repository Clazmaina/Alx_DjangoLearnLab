# CRUD Operations for Book Model

## Create

*Command:*
```python
>>> from bookshelf.models import Book
>>> book1 = Book(title="1984", author="George Orwell", publication_year=1949)
>>> book1.save()
>>> retrieved_book = Book.objects.get(title="1984")
>>> print(retrieved_book.title)
>>> print(retrieved_book.author)
>>> print(retrieved_book.publication_year)
>>> retrieved_book.title = "Nineteen Eighty-Four"
>>> retrieved_book.save()
>>> print(retrieved_book.title)
>>> retrieved_book.delete()
>>> Book.objects.get(title="Nineteen Eighty-Four") #Try to retrieve again