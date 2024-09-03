class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def mark_as_unavailable(self):
        self.is_available = False

    def mark_as_available(self):
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def display_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if available_books:
            print("Available Books:")
            for book in available_books:
                print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}")
        else:
            print("No books available in the library.")

    def display_all_books(self):
        if self.books:
            print("All Books:")
            for book in self.books:
                print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}")
        else:
            print("No books in the library.")


# Usage example:
library = Library()

book1 = Book(2122, "Java", "Meeravali")
book2 = Book(2152, "C-Language", "Sandeep")
book3 = Book(2159, "Mathematics", "Vedeep")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_all_books()

book1.mark_as_unavailable()
library.display_available_books()

library.remove_book(book2)
library.display_all_books()
