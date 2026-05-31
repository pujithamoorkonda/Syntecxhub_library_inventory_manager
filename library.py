import json
import os

class Book:
    def __init__(self, title, author, issued=False):
        self.title = title
        self.author = author
        self.issued = issued

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "issued": self.issued
        }


class Library:
    def __init__(self, filename="books.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.books = [Book(**book) for book in data]

    def save_books(self):
        with open(self.filename, "w") as file:
            json.dump(
                [book.to_dict() for book in self.books],
                file,
                indent=4
            )

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        self.save_books()

    def search_books(self, keyword):
        keyword = keyword.lower()

        return [
            book for book in self.books
            if keyword in book.title.lower()
            or keyword in book.author.lower()
        ]

    def issue_book(self, title):
        for book in self.books:
            if book.title == title and not book.issued:
                book.issued = True
                self.save_books()
                return True
        return False

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.issued:
                book.issued = False
                self.save_books()
                return True
        return False

    def report(self):
        total = len(self.books)
        issued = sum(book.issued for book in self.books)

        return {
            "total_books": total,
            "issued_books": issued,
            "available_books": total - issued
        }