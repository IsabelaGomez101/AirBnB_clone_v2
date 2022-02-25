#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    display “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_HBNB():
    """
    display “HBNB”
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """
    display “C” followed by the value of the text variable
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def display_python(text="is cool"):
    """
    display “Python ”, followed by the value of the text variable
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<n>', strict_slashes=False)
def display_number(n):
    """
    display “n is a number” only if n is an integer
    """
    try:
        n = int(n)
        return "{} is a number".format(n)
    except:
        abort(404)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_template(n):
    """
    display a HTML page only if n is an integer
    """
    return render_template('5-number.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
