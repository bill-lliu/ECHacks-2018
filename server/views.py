from .app import app


@app.route("/")
def index():
    return "Let's get this bread"
