import os
from flask import (
    Flask,
    render_template,
    redirect,
    flash,
    url_for,
    session
)
from sqlalchemy.exc import (
    IntegrityError,
    DataError,
    DatabaseError,
    InterfaceError,
    InvalidRequestError,
)
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

from datetime import timedelta
from werkzeug.routing import BuildError
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash
from run import create_app, db, login_manager, bcrypt
from models import MyMDB_User
from forms import login_form, signup_form

app = Flask(__name__)
app = create_app()

#Launch route
@app.route("/")
def index():
    return render_template("/pages/launch.html")

#Auth route
@app.route("/auth")
def auth():
    return render_template("/pages/auth.html", title='Login')

#Register route
@app.route("/register")
def register():
    return render_template("/pages/register.html", title='Register')

#Main route (login validation)
@app.route("/main", methods=("GET", "POST"))
def main():
    if form.validate_on_submit():
        try:
            user = MyMDB_Userser.query.filter_by(email=form.email.data).first()
            if check_password_hash(user.pwd, form.pwd.data):
                login_user(user)
            else:
                flash("Invalid username or password - please try again.", "login error")
        finally: return render_template("/pages/main.html", title='My Movies')

"""
error = None
if form.validate_on_submit():
    try:
        user = MyMDB_Userser.query.filter_by(email=form.email.data).first()
        if check_password_hash(user.pwd, form.pwd.data):
            login_user(user)
            return redirect(url_for('/pages/main.html'))
        else:
            flash("Invalid username or password - please try again.", "login error")
    except Exception as e:
        flash(e, "login error")
"""

@login_manager.user_loader
def load_user(user_id):
    return MyMDB_User.query.get(int(user_id))

@app.before_request
def session_handler():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)

#TODO - register route + logout session

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "8080")),
        debug=True) #TODO - change to debug=False before submitting project
