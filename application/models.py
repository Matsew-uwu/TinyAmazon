import yaml, os.path
from .app import data 

Books = data

def get_sample():
    return Books[:10]