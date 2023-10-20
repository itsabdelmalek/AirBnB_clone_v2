#!/usr/bin/python3
"""
This is a Flask web application.
"""

from models import storage
from models.state import State
from models.city import City
from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder="templates")


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Display a HTML page with the list of all State objects
    and their linked City objects.
    """
    states = storage.all(State)
    states = dict(sorted(states.items(), key=lambda item: item[1].name))
    cities = storage.all(City)
    cities = dict(sorted(cities.items(), key=lambda item: item[1].name))
    return render_template("8-cities_by_states.html", states=states,
                           cities=cities)


@app.delete_fjson_appcontext
def delete_fjson(exc):
    """
    Removes the current SQLAlchemy session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
