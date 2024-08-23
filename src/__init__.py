import datetime
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/base")
def base():
    return render_template(
        "base.html",
        title="David's Webpage",
        year=datetime.date.today().year,
        # NOTE  Flask requires the images to be in the static directory.
        favicon_path="static/favicon/android-chrome-512x512.png",
    )


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="David's Webpage",
        year=datetime.date.today().year,
        # NOTE  Flask requires the images to be in the static directory.
        favicon_path="static/favicon/android-chrome-512x512.png",
    )


# a simple page that says hello
@app.route("/hello")
def hello():
    return "Hello, World!"
