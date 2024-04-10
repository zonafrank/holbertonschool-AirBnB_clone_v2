#!/usr/bin/python3

from models.state import State
from models.city import City
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda s: s.name)
    result = []

    for state in sorted_states:
        d = {}
        d['state'] = state

        cities = sorted(state.cities, key=lambda c: c.name)
        d['cities'] = cities

        result.append(d)

    return render_template("8-cities_by_states.html", data=result)


@app.teardown_appcontext
def close_db(error):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
