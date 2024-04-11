#!/usr/bin/python3
"""Module for task 6"""

from flask import Flask, render_template
import string

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """ Prints hello hbnb string """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """ Prints hello hbnb string """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ Prints text passed in """
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    if isinstance(n, int):
        return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Prints template if number passed in """
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ Prints template to indicate if number passed in is odd or even """
    if isinstance(n, int):
        if n % 2 == 0:
            return render_template(
                "6-number_odd_or_even.html",
                val=n, even_odd="even")
        else:
            return render_template(
                "6-number_odd_or_even.html",
                val=n, even_odd="odd")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
