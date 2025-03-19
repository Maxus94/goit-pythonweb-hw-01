import logging

from abc import ABC, abstractmethod


logging.basicConfig(
    format="%(message)s", level=logging.DEBUG, handlers=[logging.StreamHandler()]
)


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):

    def show_books(self) -> None:
        for book in self.books:
            logging.info(book)


class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break


class LibraryManager:

    def __init__(self, library: Library):
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        self.library.add_book(Book(title, author, year))

    def show_books(self) -> None:
        self.library.show_books()

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)


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
                logging.error("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
