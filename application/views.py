from .app import app
from flask import render_template
from .models import get_sample, get_authors, get_books

@app.route("/")
def home():
    return render_template(
        "home.html",
        title="Selection",
        books = get_sample()
    )

@app.route("/books.html")
def books():
    return render_template(
        "home.html",
        title = "All books",
        books = get_books()
    )

@app.route("/authors.html")
def authors():
    return render_template(
        "authors.html",
        title="Authors",
        authors = get_authors()
    )