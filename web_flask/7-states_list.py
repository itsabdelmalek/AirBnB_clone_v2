#!/usr/bin/python3
"""
This is a Flask web application.
"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Display a HTML page with the list of all State objects
    sorted by name (A->Z)
    """
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.delete_fjson_appcontext
def delete_fjson(exc):
    """
    Removes the current SQLAlchemy session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
