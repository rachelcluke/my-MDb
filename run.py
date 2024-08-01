
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("/pages/launch.html")

@app.route('/auth')
def auth():
    return render_template('/pages/auth.html')

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "8080")),
        debug=True) #TODO - change to debug=False before submitting project
