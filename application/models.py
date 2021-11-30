import yaml, os.path
from .app import data, db 

# Books = data

# def get_sample():
#     return Books[:10]

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return "<Author (%d) %s>" % (self.id, self.name)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    title = db.Column(db.String(100))
    url = db.Column(db.String(100))
    img = db.Column(db.String(100))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author",
                             backref=db.backref("books", lazy="dynamic"))

    def __repr__(self):
        return "<Book (%d) %s>" % (self.id, self.title)

def get_sample():
    return Book.query.limit(10).all()


def get_books():
    return Book.query.all()


# def get_authors():
#     Author.query().order_by(Author.name.desc()).all()

# def get_books_of_author(id):
#     return Book.query.filter(
#         Book.author_id == id
#     ).all()
