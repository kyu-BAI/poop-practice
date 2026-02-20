
class Book:
    def __init__(self, title, author, is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow(self):
        borrow = input("Enter title of book you want to borrow: ")
        if borrow == self.title:
            print(f"{self.borrow}, found")
            self.is_borrowed = True
        else:
            print(f"{self.borrow}, not found")
            self.is_borrowed = False

    def return_book(self):
        r = input("Enter the title of the book you want to return:")
        if r == self.title:
            print(f"{r},returned")
            self.is_borrowed = False
        else:
            print(f"{r} does not belong to use, try another library")
    def __str__(self):
        return f"{self.title}, is authored by {self.author}"
