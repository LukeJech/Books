
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import book
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, be sure to install flask-bcrypt: pipenv install flask-bcrypt


class Author:
    db = "books_schema" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []
        # What changes need to be made above for this project?
        #What needs to be added her for class association?



    # Create Users Models
    @classmethod
    def create_author(cls, data):
        query = """
        INSERT INTO authors (name)
        VALUES (%(name)s)
        ; """

        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def create_favorite(cls, data ):
        query = """
        INSERT INTO favorites (authors_id, books_id)
        VALUES (%(authors_id)s, %(books_id)s)
        ; """
        return connectToMySQL(cls.db).query_db(query,data)

    # Read Users Models
    @classmethod
    def get_all_authors(cls):
        query = """
        SELECT * FROM authors
        ; """

        results = connectToMySQL(cls.db).query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def get_one_author(cls, author_id):
        query = """
        SELECT * FROM authors
        WHERE id = %(id)s
        """
        results = connectToMySQL(cls.db).query_db(query, {'id': author_id})
        return cls(results[0])

    @classmethod
    def get_authors_with_books(cls, author_id):
        query = """
        SELECT * FROM authors
        LEFT JOIN favorites ON favorites.authors_id = authors.id
        LEFT JOIN books ON favorites.books_id = books.id
        WHERE authors.id = %(id)s
        ; """
        results = connectToMySQL(cls.db).query_db(query, {'id':author_id})
        author = cls(results[0])
        for row_from_db in results:
            book_data = {
                'id': row_from_db['books.id'],
                'title':  row_from_db['title'],
                'num_of_pages': row_from_db['num_of_pages'],
                "created_at": row_from_db["books.created_at"],
                "updated_at": row_from_db["books.updated_at"]
            }
            author.books.append(book.Book(book_data))
        return author


    # Update Users Models



    # Delete Users Models