from flask import flash, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt 
from werkzeug.security import generate_password_hash, check_password_hash
from my_mdb import app, db
from my_mdb.models import User, LoginForm, RegisterForm

@app.route("/")
def index():
    return render_template("/pages/launch.html")

#Login
@app.route("/auth", methods=['GET', 'POST'])
def auth():
    form = LoginForm()
    if request.method=='POST': #and form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()

        if existing_user:
            print(request.form.get("username"))

            if check_password_hash(
                    existing_user[0].password, request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Hello {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "main", username=session["auth"]))
            else:
                # case - password mismatch
                flash("Incorrect Username and/or Password")
                return redirect(url_for("auth"))

        else:
            # case - username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("auth"))

    return render_template("/pages/auth.html", title='Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method=='POST': #and form.validate_on_submit():
        existing_user = User.query.filter(User.username == request.form.get("username").lower()).all()
    
        if existing_user:
            flash("This username already exists.")
            return redirect(url_for("register"))

        new_user = User(
            username=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
        )

        db.session.add(new_user)
        db.session.commit()

        session["user"] = request.form.get("username").lower()
        return redirect(url_for("main", username=session["user"]))

    return render_template("/pages/register.html", title='Register',form=form)

@app.route("/main", methods=("GET", "POST"))
def main():
    if "user" in session:
        return render_template("/pages/main.html", username=session["user"])
    return render_template("/pages/main.html", title='My Movies')

@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("auth"))
