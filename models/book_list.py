
from models.book import *


book_1 = Book("Vox", "Christina Dalcher", "Fiction")
book_2 = Book("Normal People", "Sally Rooney", "Fiction")
book_3 = Book("Bossypants", "Tina Fey", "Biography")
book_4 = Book("Invisible Women", "Caroline Criado Perez", "Non-Fiction")
book_5 = Book("Sepulchre", "Kate Mosse", "Fiction")

books = [book_1, book_2, book_3, book_4, book_5]

def add_new_book(book):
    books.append(book)


# def show_single_book(book):
#     chosen_book = books[0]






def delete_book(book_name):
    book_to_delete = None
    for book in books:
        if book.title == book_name:
            book_to_delete = book
    
        books.remove(book_1)