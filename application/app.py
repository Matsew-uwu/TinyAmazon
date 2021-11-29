from os import path
from posixpath import dirname
from flask import Flask 
import yaml, os.path
from flask_bootstrap import Bootstrap

# Application Set
app = Flask(__name__)

# Setting up Bootstrap
Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True


data = yaml.load(
    open(os.path.join(os.path.dirname(__file__), "data.yml")), 
    Loader = yaml.CLoader
)