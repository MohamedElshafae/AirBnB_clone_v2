#!/usr/bin/python3
"""doc"""
from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
