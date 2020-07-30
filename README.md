# Flask Practice
- Will be following along with Digital Ocean tutorials for building Flask applications
- [Flask](https://flask.palletsprojects.com/en/1.1.x/#user-s-guide) is a Python-based web framework that is more minimal than Django
    - Flask depends on the [Jinja](https://palletsprojects.com/p/jinja/) template engine and the [Werkzeug](https://palletsprojects.com/p/werkzeug/) WSGI toolkit
- It is the basis for [Apache Superset](https://superset.apache.org/index.html), which is "a modern, enterprise-ready business intelligence web application"
- Superset may be a good alternative to cBioPortal as a way to visualize the cBioPortal data

---
## Tutorial 1: [How To Make a Web Application Using Flask in Python 3](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3#conclusion)

### Introduction
- This tutorial will use [Bootstrap](https://getbootstrap.com/) for styling, [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) as a template engine, an [SQLite](https://sqlite.org/index.html) for its database

### Step 1 — Installing Flask
- Start by creating a conda environment (`flask_env`) and installing Flask
```
conda create --name flask_env python=3.7 (if environment doesn't already exist)
conda install --name flask_env flask
conda activate flask_env
conda deactivate
```

### Step 2 — Creating a Base Application
- In this step, you’ll make a small web application inside a Python file and run it to start the server, which will display some information on the browser.
- Create and enter your `flask_blog` directory, create the application in `hello.py`
- To run your web application, you’ll first tell Flask where to find the application (the `hello.py` file in your case) with the `FLASK_APP` environment variable:
```
export FLASK_APP=hello
```
- Then run it in development mode with the `FLASK_ENV` environment variable:
```
export FLASK_ENV=development
```
- Lastly, run the application using the flask run command:
```
flask run
```
- App should now be running on `localhost:5000`

### Step 3 — Using HTML templates
- Flask provides a `render_template()` helper function that allows use of the Jinja template engine.
- This allows you to use HTML files, (*templates*) to build all of your application pages, such as the main page where you’ll display the current blog posts, the page of the blog post, the page where the user can add a new post, and so on.
- This is done in the `app.py` file of `flask_blog`
- HTML templates will be placed in `flask_blog/templates/`
- In addition to the `templates` folder, Flask web applications also typically have a `static` folder for hosting static files, such as CSS files (in `css` subfolder), JavaScript files (in `js` subfolder), and images (in `images` or `img` subfolder) the application uses.
    - You can create a `style.css` style sheet file to add CSS to your application and place it in `flask_blog/static/css/`
- To re-run new application:
```
export FLASK_APP=app
flask run
```
- You can avoid unnecessary code repetition with the help of a base template file, which all of your HTML files will inherit from.
    - See [Template Inheritance in Jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/#template-inheritance) for more information
- The base template `base.html` can now be extended by `index.html`
    - *Note: `base.html` makes use of Bootstrap for styling*

### Step 4 — Setting up the Database
- In this step, you’ll set up a database to store data, that is, the blog posts for your application. You’ll also populate the database with a few example entries.
- You’ll use a SQLite database file to store your data because the `sqlite3` module, which we will use to interact with the database, is readily available in the standard Python library.
- Will store the blog post data in a table called `post`
    - Will place the SQL command in `flask_blog/schema.sql`
- Now that you have a SQL schema in the `schema.sql` file, you’ll use it to create the database using a Python file named `init_db.py` inside the `flask_blog` directory, that will generate an SQLite `.db` database file.
    - Run `python init_db.py` to set up database

### Step 5 — Displaying All Posts
- Now that you’ve set up your database, you can now modify the `index()` view function to display all the posts you have in your database.

### Step 6 — Displaying a Single Post
- In this step, you’ll create a new Flask route with a view function and a new HTML template to display an individual blog post by its ID.
- By the end of this step, the URL `http://127.0.0.1:5000/ID` URL will display the post with the associated `ID` number if it exists
    - For example, `http://127.0.0.1:5000/1` will be a page that displays the first post (because it has the ID `1`).
- The `post.html` template is used to display a single post

### Step 7 — Modifying Posts
- Need to allow the users of your application to write new blog posts and add them to the database, edit the existing ones, and delete unnecessary blog posts.

#### Creating a New Post
- In this section, you’ll create a page on which you will be able to create a post by providing its title and content.
- You will make use of the `flash()` function which stores flashed messages in the client's browser session, and makes use of a secret key
- More on this can be found in Flask's [session documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions)
    - For more on cookies and sessions, [check this out](https://www.guru99.com/difference-between-cookie-session.html)
- `create.html` is the HTML template for blog post creation

#### Editing a Post
- For a blog to be up to date, you’ll need to be able to edit your existing posts.
- This section will guide you through creating a new page in your application to simplify the process of editing a post.
- `edit.html` is the HTML template for editing an existing blog post.

#### Deleting a Post
- Sometimes a post no longer needs to be publicly available, which is why the functionality of deleting a post is crucial.
- In this step you will add the delete functionality to your application.

---
## Tutorial 2: [How To Serve Flask Applications with Gunicorn and Nginx on CentOS 7](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-centos-7)
- I am hoping this tutorial gives me a greater depth of understanding of what all goes into making a nearly production-ready Flask app






~~end~~
