#!/usr/bin/python3
"""Module for task 1"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returns a string literal response"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns a string literal response"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
