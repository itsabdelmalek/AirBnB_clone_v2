#!/usr/bin/python3
"""
This is a simple Flask web application.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays "Hello HBNB!".
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")