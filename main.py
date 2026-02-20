from models.book import Book
from models.member import Member
from services.library import Library


def main():
    library = Library()

    while True:
        print("\n=== LIBRARY MENU ===")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Show Available Books")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Book title: ")
            author = input("Author: ")
            library.add_book(Book(title, author))

        elif choice == "2":
            name = input("Member name: ")
            library.add_member(Member(name))

        elif choice == "3":
            member = library.find_member(input("Member name: "))
            book = library.find_book(input("Book title: "))

            if member and book:
                library.borrow_book(member, book)
            else:
                print("Member or book not found")

        elif choice == "4":
            member = library.find_member(input("Member name: "))
            book = library.find_book(input("Book title: "))

            if member and book:
                library.return_book(member, book)
            else:
                print("Member or book not found")

        elif choice == "5":
            library.show_available_books()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
