# Assignment 11: Class Methods
class Book:
    total_books = 0  # class variable

    def __init__(self, title):
        self.title = title
        Book.total_books += 1

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Example usage
book1 = Book("Python Basics")
book2 = Book("Advanced Python")
Book.increment_book_count()
print(Book.total_books)  # Output: 3