from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import book_model

class Author:
    DB ='books_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.all_favorite_books = []

    @classmethod
    def get_all_authors(cls):
        query = """
        SELECT * FROM authors;
        """

        results = connectToMySQL(cls.DB).query_db(query)

        all_authors = []

        for author in results:
            all_authors.append(cls(author))

        return all_authors
    
    @classmethod
    def add_author(cls, data):
        query = """
        INSERT INTO authors (name)
        VALUES (%(name)s);
        """

        results = connectToMySQL(cls.DB).query_db(query, data)

        return results
    
    @classmethod
    def get_authors_favorites(cls, data):
        query = """
        SELECT * FROM books
        JOIN favorites
        ON books.id = favorites.book_id
        JOIN authors
        ON authors.id = favorites.author_id
        WHERE author_id = %(id)s;
        """

        results = connectToMySQL(cls.DB).query_db(query, data)

        all_authors_favorites = [];

        for book in results:
            all_authors_favorites.append(book)

        return all_authors_favorites
    
    @classmethod
    def get_one_author(cls, data):
        query = """
        SELECT * FROM authors
        WHERE id = %(id)s;
        """

        results = connectToMySQL(cls.DB).query_db(query, data)

        return cls(results[0])
    
    @classmethod
    def add_favorite(cls, data):
        query = """
        INSERT INTO favorites (author_id, book_id)
        VALUES (%(author_id)s, %(book_id)s)
        """

        results = connectToMySQL(cls.DB).query_db(query, data)

        return results