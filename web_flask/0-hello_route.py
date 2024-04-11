#!/usr/bin/python3
"""Module for task 0"""

from flask import Flask
"""Module for task 0: creates a basic flask app"""

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returns a string literal response"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
