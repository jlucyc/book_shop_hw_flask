from flask import render_template, request, redirect
from app import app
from models.book_list import books, add_new_book, delete_book
from models.book import *





@app.route('/books')
def index():
    return render_template('index.html', title='Home', books=books)




@app.route('/books', methods=['POST'])
def add_book():
    title = request.form['Title']
    author = request.form['Author']
    genre = request.form['Genre']
    newbook = Book(title=title, author=author, genre=genre)
    add_new_book(newbook)
    return redirect('/books')

# @app.route('/books/<index>')
# def single_book(index):
#     chosen_book = books[int(index)]
#     return render_template('base.html', order=chosen_book)


@app.route('/books/delete/<title>/', methods=['POST'])
def remove(title):
    delete_book(title)
    return redirect('/books') 
