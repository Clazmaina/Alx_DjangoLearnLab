from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Create some sample data
    author1 = Author.objects.create(name="Jane Austen")
    author2 = Author.objects.create(name="Leo Tolstoy")

    book1 = Book.objects.create(title="Pride and Prejudice", author=author1)
    book2 = Book.objects.create(title="Emma", author=author1)
    book3 = Book.objects.create(title="War and Peace", author=author2)

    library1 = Library.objects.create(name="Main Library")
    library1.books.add(book1, book2)
    library2 = Library.objects.create(name="Branch Library")
    library2.books.add(book3)

    librarian1 = Librarian.objects.create(name="Alice", library=library1)
    librarian2 = Librarian.objects.create(name="Bob", library=library2)

    # Query examples
    print("Books by Jane Austen:")
    books_by_jane = Book.objects.filter(author=author1)
    for book in books_by_jane:
        print(book.title)

    print("\nBooks in Main Library:")
    books_in_main = library1.books.all()
    for book in books_in_main:
        print(book.title)

    print("\nLibrarian for Branch Library:")
    librarian_branch = Librarian.objects.get(library=library2)
    print(librarian_branch.name)

if __name__ == "__main__":
    run_queries()