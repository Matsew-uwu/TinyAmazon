from os import path
from posixpath import dirname
from flask import Flask 
import yaml, os.path

app = Flask(__name__)
data = yaml.load(
    open(os.path.join(os.path.dirname(__file__), "data.yml")), 
    Loader = yaml.CLoader
)