from flask import Flask, render_template

def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.jinja2")

    return app
