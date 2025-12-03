class Book:
    def __init__(self, title, author):
        """Base class for all books."""
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author, file_size):
        """EBook inherits from Book and adds file size."""
        super().__init__(title, author)
        self.file_size = file_size  # in KB


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """PrintBook inherits from Book and adds page count."""
        super().__init__(title, author)
        self.page_count = page_count  # number of pages


class Library:
    def __init__(self):
        """Library uses composition: it 'has a' list of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
