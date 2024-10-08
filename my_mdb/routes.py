from flask import flash, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt 
from werkzeug.security import generate_password_hash, check_password_hash
from my_mdb import app, db
from my_mdb.models import User, Movie, LoginForm, RegisterForm, AddMovieForm, EditMovieForm

@app.route("/")
def index():
    return render_template("/pages/launch.html")

#Login
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method=='POST':
        existing_user = User.query.filter(User.username == \
                                    request.form.get("username").lower()).first()

        if existing_user:
            print(request.form.get("username"))

            if check_password_hash(
                    existing_user.password, request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        session["user_id"] = existing_user.id
                        return redirect(url_for(
                            "my_movies", username=session["user"]))
            else:
                # case - password mismatch
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # case - username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

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
        return redirect(url_for("my_movies", username=session["user"]))

    return render_template("/pages/register.html", title='Register',form=form)

@app.route("/my_movies", methods=("GET", "POST"))
def my_movies():
    if "user" in session:
        movies = list(Movie.query.filter(Movie.user_id==session["user_id"]).order_by(Movie.view_date.desc()))
        return render_template("/pages/main.html", username=session["user"], movies=movies)

    return render_template("/pages/main.html", title='My Movies', movies=movies)

@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if request.method == "POST":
        
        new_movie = Movie(
            movie_name=request.form.get("movie_name"),
            movie_review=request.form.get("movie_review"),
            view_date=request.form.get("view_date"),
            user_id=session["user_id"]
        )

        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("my_movies"))
        
    return render_template("/pages/addMoviePage.html", title='Add Movie',form=form)

@app.route("/delete_movie/<int:movie_id>")
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("my_movies"))

@app.route("/edit_movie/<int:movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    form = EditMovieForm()

    if request.method == "POST":
        movie.movie_review=request.form.get("movie_review"),
        movie.view_date=request.form.get("view_date"),
        db.session.commit()
        return redirect(url_for("my_movies"))

    return render_template("/pages/editMoviePage.html",title='Edit Movie', form=form, movie=movie)

#TODO add validation for entry (ex, movie duplicate, match with API)

@app.route("/community", methods=("GET", "POST"))
def community():
    if "user" in session:
        movies = list(Movie.query.order_by(Movie.view_date.desc()).all())
        return render_template("/pages/community.html", username=session["user"], movies=movies)

    return render_template("/pages/community.html", title='My Movies', movies=movies)