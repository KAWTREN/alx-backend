#!/usr/bin/env python3
"""doc doc"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """doc doc """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
