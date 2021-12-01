from .app import app
from flask import render_template
from .models import get_sample, get_authors, get_books

from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField
from wtforms.validators import DataRequired

class AuthorForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Nom', validators=[DataRequired()])

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

@app.route("/edit/author/<int:id>")
def edit_author(id):
    a = get_author(id)
    f = AuthorForm(id=a.id, name=a.name)
    return render_template(
        "edit-author.html",
        author=a, form=f
    )