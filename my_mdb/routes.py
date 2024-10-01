from flask import flash, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt 
from werkzeug.security import generate_password_hash, check_password_hash
from my_mdb import app, db
from my_mdb.models import User, Movie, LoginForm, RegisterForm, AddMovieForm

@app.route("/")
def index():
    return render_template("/pages/launch.html")

#Login
@app.route("/auth", methods=['GET', 'POST'])
def auth():
    form = LoginForm()
    if request.method=='POST':
        existing_user = User.query.filter(User.username == \
                                    request.form.get("username").lower()).all()

        if existing_user:
            print(request.form.get("username"))

            if check_password_hash(
                    existing_user[0].password, request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        return redirect(url_for(
                            "main", username=session["user"]))
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
    if request.method=='POST':
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

@app.route("/addMoviePage", methods=["GET", "POST"])
def addMoviePage():
    form = AddMovieForm()
    if request.method == "POST":
        
        new_movie = Movie(
            movie_name=request.form.get("movie_name"),
            movie_review=request.form.get("movie_review"),
            view_date=request.form.get("view_date")
        )

        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("main"))
        
    return render_template("/pages/addMoviePage.html", title='Add Movie',form=form)

#TODO add validation for entry (ex, movie duplicate, match with API)