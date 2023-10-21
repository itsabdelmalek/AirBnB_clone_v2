#!/usr/bin/python3
"""
This is a Flask web application.
"""

from models import storage
from models.state import State
from models.city import City
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """
    Displays a HTML page with the list of all State objects
    present in DBStorage sorted by name (A->Z)
    """
    states = storage.all(State).values()
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    Displays a HTML page with the details of a specific State
    including linked City objects.
    """
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template("9-states.html", state=state, cities=cities)
    else:
        return render_template("9-states.html", not_found=True)


@app.teardown_appcontext
def teardown(exception):
    """
    Removes the current SQLAlchemy session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
