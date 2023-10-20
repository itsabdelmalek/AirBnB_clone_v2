#!/usr/bin/python3
"""
This is a Flask web application.
"""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder="templates")


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Display a HTML page with the list of all State objects
    sorted by name (A->Z)
    """
    states = storage.all("State")
    states = dict(sorted(states.items(), key=lambda item: item[1].name))
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(error):
    """
    Removes the current SQLAlchemy session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
