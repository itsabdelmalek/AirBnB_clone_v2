#!/usr/bin/python3
"""
This is a Flask web application.
"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """
    Displays a HTML page with the list of all State objects
    present in DBStorage sorted by name (A->Z)
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    Displays a HTML page with the details of a specific State
    including linked City objects.
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.delete_fjson_appcontext
def delete_fjson(exc):
    """
    Removes the current SQLAlchemy session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
