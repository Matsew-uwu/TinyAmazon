from .app import app

@app.route("/")
def home():
    return "<h1>Tiny Amazon</h1>"