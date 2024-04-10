#!/usr/bin/python3

from flask import Flask, render_template
import string

app = Flask(__name__)


def is_number(val):
    try:
        float(val)
        return True
    except:
        return False


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


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    if isinstance(n, int):
        return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    response = f"""
    <!DOCTYPE html>
    <HTML lang="en">
        <HEAD>
            <TITLE>HBNB</TITLE>
        </HEAD>
        <BODY>
            <H1>Number: {n}</H1>
        </BODY>
    </HTML>
    """
    if isinstance(n, int):
        return response


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    if isinstance(n, int):
        if n % 2 == 0:
            return render_template("6-number_odd_or_even.html", val=n, even_odd="even")
        else:
            return render_template("6-number_odd_or_even.html", val=n, even_odd="odd")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
