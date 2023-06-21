from flask_app import app
from flask import render_template, request, redirect, session

from flask_app.models.book_model import Book
from flask_app.models.author_model import Author

@app.route('/books')
def show_books():

    all_books = Book.get_all_books()

    return render_template('books.html', all_books = all_books)

@app.route('/create_book', methods = ['POST'])
def create_book():

    Book.add_book(request.form)

    return redirect('/books')

@app.route('/books/<int:book_id>')
def show_book_page(book_id):

    one_book = Book.get_one_book({'id' : book_id})

    one_book_favorites = Book.get_books_favorites({'id' : book_id})

    all_authors = Author.get_all_authors()

    return render_template('addbook.html', one_book = one_book, one_book_favorites = one_book_favorites, all_authors = all_authors)

@app.route('/create_books_favorite/<int:book_id>', methods =['POST'])
def create_books_favorite(book_id):

    Book.get_one_book({'id' : book_id})

    Book.add_favorite(request.form)

    return redirect('/books')

