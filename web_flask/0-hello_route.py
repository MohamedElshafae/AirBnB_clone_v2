#!/usr/bin/python3
"""doc"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def homepage():
    """doc"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)