from models.book import Book
from models.member import Member


class Library:
    def __init__(self):
        self.books = []
        self.members

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.book.append(new_book)

    def add_member(self, name):
        new_member = Member(name)
        self.members.append(new_member)

    def bb(self, member_object, book_object):
        print(f"{book_object.title}, borrowed by {member_object.name}")

    def rr(self, member_object, book_object):
        print(f"{book_object.title}, returned by {member_object.name}")
