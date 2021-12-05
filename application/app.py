from os import path
from posixpath import dirname
from flask import Flask 
import yaml, os.path
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

# Application Set
app = Flask(__name__)

# Setting up Bootstrap
Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

# Setting up sqlqlchemy
def mkpath(p):
    return path.normpath(
        path.join(os.path.dirname(__file__), p)
    )

app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///' + mkpath('../myapp.db'))
app.config['SECRET_KEY'] = "d7bf876c-777f-4d07-b5ca-b83facddd66d"
db = SQLAlchemy(app)



data = yaml.load(
    open(os.path.join(os.path.dirname(__file__), "data.yml")), 
    Loader = yaml.CLoader
)