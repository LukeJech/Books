from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import author
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, be sure to install flask-bcrypt: pipenv install flask-bcrypt


class Book:
    db = "books_schema" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []
        # What changes need to be made above for this project?
        #What needs to be added her for class association?



    # Create Users Models
    @classmethod
    def create_book(cls, data):
        query = """
        INSERT INTO books (title, num_of_pages)
        VALUES (%(title)s, %(num_of_pages)s)
        ; """

        return connectToMySQL(cls.db).query_db(query, data)


    # Read Users Models
    @classmethod
    def get_all_books(cls):
        query = """
        SELECT * FROM books
        ; """

        results = connectToMySQL(cls.db).query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books
    
    @classmethod
    def get_one_book(cls, book_id):
        query = """
        SELECT * FROM books
        WHERE id = %(id)s
        ; """
        results = connectToMySQL(cls.db).query_db(query, {'id':book_id})
        return cls(results[0])
    
    @classmethod
    def get_books_with_authors(cls, book_id):
        query = """
        SELECT * FROM books
        LEFT JOIN favorites ON favorites.books_id = books.id
        LEFT JOIN authors ON favorites.authors_id = authors.id
        WHERE books.id = %(id)s
        ; """
        results = connectToMySQL(cls.db).query_db(query, {'id':book_id})
        book = cls(results[0])
        for row_from_db in results:
            author_data = {
                'id': row_from_db['authors.id'],
                'name':  row_from_db['name'],
                "created_at": row_from_db["authors.created_at"],
                "updated_at": row_from_db["authors.updated_at"]
            }
            book.authors.append(author.Author(author_data))
        return book



    # Update Users Models



    # Delete Users Models