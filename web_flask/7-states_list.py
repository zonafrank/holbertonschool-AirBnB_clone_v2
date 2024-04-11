#!/usr/bin/python3
"""Module for task 8"""

from models.state import State
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ Returns HTML lisitng out all States """
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda s: s.name)

    return render_template("7-states_list.html", states=sorted_states)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
