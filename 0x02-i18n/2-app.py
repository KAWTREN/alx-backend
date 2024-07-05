#!/usr/bin/env python3
"""doc doc"""
from flask import Flask, render_template, request
from flask_babel import Babel  # type: ignore


class Config:
    """doc doc"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localselector
def get_locale():
    """DOC DOC"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """doc doc """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
