#!/usr/bin/python3
"""Module for task 2"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """returns a string literal response"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """returns a string literal response"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ returns text passed in as route parameter"""
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
