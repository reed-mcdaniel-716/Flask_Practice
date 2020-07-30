# for SQLite database
import sqlite3

# again importing the Flask object
# render_template helper function lets you render HTML template files that exist in the templates folder
# global request object to access incoming request data that will be submitted via an HTML form.
# url_for() function to generate URLs.
# flash() function to flash a message when a request is processed.
# redirect() function to redirect the client to a different location.
from flask import Flask, render_template, request, url_for, flash, redirect

# for responding to unsucessful requests with 404 error
from werkzeug.exceptions import abort

# function to get a blog post by its ID from the database
# You can call it by passing it an ID and receive back the blog post associated with the provided ID, or make Flask respond with a 404 Not Found message if the blog post does not exist.
def get_post(post_id):
    conn = get_db_connection()
    # getting first result matching criteria, as there should be at most one (IDs are unique)
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

# function for connecting to our database containing blog post table
def get_db_connection():
    conn = sqlite3.connect('database.db')
    # sets the row_factory attribute to sqlite3.Row so you can have name-based access to columns
    # This means that the database connection will return rows that behave like regular Python dictionaries
    conn.row_factory = sqlite3.Row
    # returns connection object
    return conn

# Flask application instance called app
app = Flask(__name__)

# The flash() function stores flashed messages in the client’s browser session, which requires setting a secret key.
# This secret key is used to secure sessions, which allow Flask to remember information from one request to another, such as moving from the new post page to the index page.
# The user can access the information stored in the session, but cannot modify it unless they have the secret key, so you must never allow anyone to access your secret key.

# To set a secret key, you’ll add a SECRET_KEY configuration to your application via the app.config object.
app.config['SECRET_KEY'] = 'super secret key'
#---------------------------------------------------------------
# Routing
# Flask uses Werkzeug to handle routing, and it orders routes based on how many variable parts are in the route.
# help from: https://stackoverflow.com/questions/25011782/are-python-flask-order-of-routes-defined
# route decorator for URL / i.e. main URL
@app.route('/')
# The index() view function returns the result of calling render_template() with index.html as an argument
def index():
    conn = get_db_connection()
    # the fetchall() method will fetch all the rows of the query result i.e. all blog posts
    # creates a list of dictionary-like objects
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    # rendering index.html and passing in posts as an argument
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
# variable rule <int:post_id> to specifies that the part after the slash (/) is a positive integer (marked with the int converter) that you need to access in your view function.
# Flask recognizes this and passes its value to the post_id keyword argument of your post() view function.
def post(post_id):
    # use the get_post() function to get the blog post associated with the specified ID and store the result in the post variable
    post = get_post(post_id)
    # passing post to the post.html template
    return render_template('post.html', post=post)

# for creating blog posts
# view function will accept both GET and POST requests
@app.route('/create', methods=('GET', 'POST'))
def create():
    # if request is a POST request
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
            conn.commit()
            conn.close()
            # redirecting to the homepage upon completion
            return redirect(url_for('index'))
    # GET requests will automatically return blank creation template
    return render_template('create.html')

# for editing blog posts
# view function will accept both GET and POST requests
@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    # getting post by id provided as argument to view function
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?', (title, content, id))
            conn.commit()
            conn.close()
            # redirect to homepage
            return redirect(url_for('index'))
    # GET requests will automatically return edit template filled in with info from post
    return render_template('edit.html', post=post)

# for deleting blog posts
# view function only accepts post requests
# you can access this route via a form that sends a POST request passing in the ID of the post you want to delete
    # will add this function to the post edit template
# the function will receive the ID value and use it to get the post from the database with the get_post() function.
@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))














#
