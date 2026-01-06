from flask import Flask, render_template

from endpoints import api_bp

app = Flask(__name__)


app.register_blueprint(api_bp)


@app.get("/")
def read_root():
    return render_template("index.html")


# <a href="/api/data">Get Data →</a>
