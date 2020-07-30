# import the Flask object from the flask package
from flask import Flask

# creating a Flask application instance with name app
# __name__ holds the name of the current Python module
app = Flask(__name__)

# Once you create the app instance, you use it to handle incoming web requests and send responses to the user.
# @app.route is a decorator that turns a regular Python function into a Flask view function, which converts the function’s return value into an HTTP response to be displayed by an HTTP client, such as a web browser.
# You pass the value '/' to @app.route() to signify that this function will respond to web requests for the URL /, which is the main URL.
@app.route('/')

# The hello() view function returns the string 'Hello, World!' as a response.
def hello():
    return 'Hello, World!'
