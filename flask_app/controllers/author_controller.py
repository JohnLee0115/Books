from flask_app import app
from flask import render_template, request, redirect, session

from flask_app.models.author_model import Author
from flask_app.models.book_model import Book

@app.route('/')
def send_to_authors():
    return redirect('/authors')

@app.route('/authors')
def show_authors():

    all_authors = Author.get_all_authors()

    return render_template('index.html', all_authors = all_authors)

@app.route('/create_author', methods = ['POST'])
def create_author():

    Author.add_author(request.form)

    return redirect('/')

@app.route('/authors/<int:author_id>')
def show_author_page(author_id):

    one_author = Author.get_one_author({'id' : author_id})

    one_author_favorites = Author.get_authors_favorites({'id' : author_id})

    all_books = Book.get_all_books()

    return render_template('author.html', one_author_favorites = one_author_favorites, all_books = all_books, one_author = one_author)

@app.route('/create_authors_favorite/<int:author_id>', methods =['POST'])
def create_authors_favorite(author_id):

    Author.get_one_author({'id' : author_id})

    Author.add_favorite(request.form)

    return redirect(f'/authors/{author_id}')
