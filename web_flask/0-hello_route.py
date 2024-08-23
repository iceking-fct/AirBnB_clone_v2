#!/usr/bin/python3
"""A script that starts a simple web flask application"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """defines the base app route, and prints hello hbnb at the root"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
