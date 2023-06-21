from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import author_model

class Book:
    DB ='books_schema'
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.all_favorited_authors = []

    @classmethod
    def get_all_books(cls):
        query = """
        SELECT * FROM books;
        """

        results = connectToMySQL(cls.DB).query_db(query)

        all_books = []

        for book in results:
            all_books.append(cls(book))

        return all_books
    
    @classmethod
    def add_book(cls, data):
        query = """
        INSERT INTO books (title, num_of_pages)
        VALUES (%(title)s, %(num_of_pages)s)
        """

        results = connectToMySQL(cls.DB).query_db(query, data)

        return results
    
    @classmethod
    def get_one_book(cls, data):
        query = """
        SELECT * FROM books
        WHERE id = %(id)s;
        """

        results = connectToMySQL(cls.DB).query_db(query, data)

        return cls(results[0])
    
    @classmethod
    def get_books_favorites(cls, data):
        query = """
        SELECT * FROM authors
        JOIN favorites
        ON authors.id = favorites.author_id
        JOIN books
        ON books.id = favorites.book_id
        WHERE book_id = %(id)s
        """

        results = connectToMySQL(cls.DB).query_db(query, data)

        all_books_favorites = [];

        for author in results:
            all_books_favorites.append(author)

        return all_books_favorites
    
    @classmethod
    def add_favorite(cls, data):
        query = """
        INSERT INTO favorites (book_id, author_id)
        VALUES (%(book_id)s, %(author_id)s)
        """

        results = connectToMySQL(cls.DB).query_db(query, data)

        return results

