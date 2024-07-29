
import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("components/background.html")

@app.route("/launch")
def launch():
    return render_template("launch.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True) #TODO - change to debug=False before submitting project
