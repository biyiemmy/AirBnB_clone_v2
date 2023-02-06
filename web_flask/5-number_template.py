#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
    /number/<n>: Displays 'n is a number' only if <n> is an integer.
    /number_template/<n>: Displays an HTML page only if <n> is an integer.
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace("_", " ")
    return "C " + text


@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    text = text.replace("_", " ")
    return "Python " + text


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    try:
        n = int(n)
        return str(n) + " is a number"
    except ValueError:
        return n + " is not a number"


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    try:
        n = int(n)
        return render_template("number.html", number=n)
    except ValueError:
        return n + " is not a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
