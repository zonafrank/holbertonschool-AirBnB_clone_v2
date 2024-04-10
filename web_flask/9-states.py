#!/usr/bin/python3

from models.state import State
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_list(id=None):
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda s: s.name)
    data = []
    id_found = False

    for state in sorted_states:
        item = {}
        item["state"] = state

        if state.id == id:
            id_found = True

        item["cities"] = sorted(state.cities, key=lambda city: city.name)
        data.append(item)

    return render_template("9-states.html", data=data, id=id, id_found=id_found)


@app.teardown_appcontext
def close_db(error):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
