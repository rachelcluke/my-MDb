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
from app import create_app,db, login_manager,bcrypt
from models import MyMDB_User
from forms import login_form, signup_form

#Launch route
@app.route("/")
def index():
    return render_template("/pages/launch.html")

#Login route
@app.route("/auth", methods=("GET", "POST"))
def auth():
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(email=form.email.data).first()
            if check_password_hash(user.pwd, form.pwd.data):
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash("Invalid username or password - please try again.", "login error")
        except Exception as e:
            flash(e, "login error")

    return render_template("/pages/auth.html")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "8080")),
        debug=True) #TODO - change to debug=False before submitting project

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app = create_app()

@app.before_request
def session_handler():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)

#TODO - register route + logout session