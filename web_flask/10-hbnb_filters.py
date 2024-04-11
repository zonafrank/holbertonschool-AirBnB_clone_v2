#!/usr/bin/python3
"""Module for task 11"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def states_list():
    """ Returns HTML lisitng out all Cities by their States """
    states_data = []
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda s: s.name)

    amenities = storage.all(Amenity)
    amenity_names = sorted([item.name for item in amenities.values()])

    for state in sorted_states:
        item = {}
        item["state"] = state

        item["cities"] = sorted(state.cities, key=lambda city: city.name)
        states_data.append(item)

    return render_template(
        "10-hbnb_filters.html",
        data={"states": states_data, "amenities": amenity_names})


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
