from abc import ABC, abstractmethod

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    
    def show_books(self):
        for book in self.books:            
            print(book)

class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
    
class LibraryManager:
    
    def __init__(self, library: Library):
        self.library = library

    def add_book(self, title, author, year):
        self.library.add_book(Book(title, author, year))

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break    



def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()


# def main():
#     library = Library()
    
#     while True:
#         command = input("Enter command (add, remove, show, exit): ").strip().lower()
        
#         if command == "add":
#             title = input("Enter book title: ").strip()
#             author = input("Enter book author: ").strip()
#             year = input("Enter book year: ").strip()
#             book = Book(title, author, year)
#             library.add_book(book)
#         elif command == "remove":
#             title = input("Enter book title to remove: ").strip()
#             library.remove_book(title)
#         elif command == "show":
#             library.show_books()
#         elif command == "exit":
#             break
#         else:
#             print("Invalid command. Please try again.")

# if __name__ == "__main__":
#     main()


