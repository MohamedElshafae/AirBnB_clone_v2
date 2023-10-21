#!/usr/bin/python3
"""doc"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def homepage():
    """doc"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """doc"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display(text):
    """doc"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """doc"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """doc"""
    if isinstance(n, int):
        return f'{n} is a number'
    return None


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """doc"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)
    return None


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def is_odd_or_even(n):
    """doc"""
    num = ""
    if isinstance(n, int):
        if n % 2 == 0:
            num = f'{n} is even'
        else:
            num = f'{n} is odd'
        return render_template('6-number_odd_or_even.html', is_even_odd=num)
    return None


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
