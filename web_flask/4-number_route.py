#!/usr/bin/python3

from flask import Flask, abort
import string

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<n>", strict_slashes=False)
def number_route(n):
    if (n and n.isdigit()):
        return f"{n} is a number"
    abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
