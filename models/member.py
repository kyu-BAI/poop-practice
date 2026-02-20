from .book import Book
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    def borrow_book(self, book_object):
        b = input("Enter the title of the book you want to borrow: ")
        if b == book_object.title:
            print(f"{b} Found!")
            self.borrowed_books.append(b)
        else:
            print(f"{b} not found, try another library")
    def member_return (self, book_object):
        r = input("Enter the title of the book that you want to return: ")
        if r == book_object.title:
            print(f'{r} has been returned!')
            self.borrowed_books.remove(r)
        else:
            print(f"{r} is not a book from our library!")