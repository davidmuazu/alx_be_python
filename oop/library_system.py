# Base Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived Class
class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call the base class constructor
        super().__init__(title, author)
        self.file_size = file_size  # extra attribute for EBook

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived Class: PrintBook (inherits from Book)
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call the base class constructor
        super().__init__(title, author)
        self.page_count = page_count  # extra attribute for PrintBook

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition: Library contains books
class Library:
    def __init__(self):
        self.books = []  # list to hold any type of Book

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)  # Automatically calls each object's __str__()
