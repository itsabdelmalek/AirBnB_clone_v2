#!/usr/bin/python3
"""
This is a Flask web application.
"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_context(exception):
    """
    Removes the current SQLAlchemy session.
    """
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def state_id(id=None):
    """Render state by id
    """
    states = storage.all("State").values()
    cities = storage.all("City").values()
    return render_template("9-states.html",
                           states=states, cities=cities, id=id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
