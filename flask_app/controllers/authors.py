from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import author # import entire file, rather than class, to avoid circular imports

# Create Users Controller
@app.route('/create/author', methods=['POST'])
def create_author():
    #use author model to create a new database entry
    author_id = author.Author.create_author(request.form)

    return redirect(f'/author/{author_id}')


# Read Users Controller

@app.route('/authors')
def authors_page():
    return render_template('authors.html', authors = author.Author.get_all_authors())

@app.route('/author/<int:author_id>')
def author_page(author_id):
    return render_template('author_page.html', author = author.Author.get_one_author(author_id))


# Update Users Controller



# Delete Users Controller


# Notes:
# 1 - Use meaningful names
# 2 - Do not overwrite function names
# 3 - No matchy, no worky
# 4 - Use consistent naming conventions 
# 5 - Keep it clean
# 6 - Test every little line before progressing
# 7 - READ ERROR MESSAGES!!!!!!
# 8 - Error messages are found in the browser and terminal




# How to use path variables:
# @app.route('/<int:id>')
# def index(id):
#     user_info = user.User.get_user_by_id(id)
#     return render_template('index.html', user_info)

# Converter -	Description
# string -	Accepts any text without a slash (the default).
# int -	Accepts integers.
# float -	Like int but for floating point values.
# path 	-Like string but accepts slashes.