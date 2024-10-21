from flask import flash, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt 
from werkzeug.security import generate_password_hash, check_password_hash
from my_mdb import app, db
from my_mdb.models import User, Movie, LoginForm, RegisterForm, AddMovieForm, EditMovieForm
from validation import check_for_empty_field, check_input_length, check_date_format, check_date_entry

@app.route("/")
def index():
    return render_template("/pages/launch.html")

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
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            flash("Username does not exist")
            return redirect(url_for("login"))

    return render_template("/pages/auth.html", title='Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method=='POST':
        form_username = request.form.get("username")
        form_password = request.form.get("password")
        existing_user = User.query.filter(User.username == form_username.lower()).all()
        is_username_empty = check_for_empty_field(form_username)
        is_password_empty = check_for_empty_field(form_password)
        is_username_length_validated = check_input_length(form_username,4,15)
        is_password_length_validated = check_input_length(form_password,8,20)
    
        if existing_user:
            flash("This user already exists.")
            return redirect(url_for("register"))
        elif (is_username_empty == True)|(is_password_empty == True):
            flash("Username/ Password cannot be empty.")
            return redirect(url_for("register"))
        elif (is_password_length_validated == False):
            flash("Password must be between 8-20 characters.")
            return redirect(url_for("register"))
        elif (is_username_length_validated == False):
            flash("Username must be between 4-15 characters.")
            return redirect(url_for("register"))
        else:
            new_user = User(
                username=request.form.get("username").lower(),
                password=generate_password_hash(request.form.get("password"))
            )
            db.session.add(new_user)
            db.session.commit()

            session["user"] = request.form.get("username").lower()
            return redirect(url_for("my_movies", username=session["user"]))

    return render_template("/pages/register.html", title='Register',form=form)

@app.route("/my-movies", methods=("GET", "POST"))
def my_movies():
    if "user" in session:
        movies = list(Movie.query.filter(Movie.user_id==session["user_id"]).order_by(Movie.view_date.desc()))
        return render_template("/pages/main.html", username=session["user"], movies=movies)

    return render_template("/pages/main.html", title='My Movies', movies=movies)

@app.route("/logout")
def logout():
    session.pop("user")
    flash("You have been logged out")
    return redirect(url_for("login"))

@app.route("/add-movie", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if request.method == "POST":

        is_movie_name_filled = check_for_empty_field(request.form.get("movie_name"))
        is_review_filled = check_for_empty_field(request.form.get("movie_review"))
        is_date_filled = check_for_empty_field(("view_date"))
        is_movie_name_length_validated = check_input_length((request.form.get("movie_name")),1,50)
        is_movie_review_length_validated = check_input_length((request.form.get("movie_review")),1,20)
        is_date_format_validated = check_date_format(request.form.get("view_date"))
        is_date_entry_validated = check_date_entry(request.form.get("view_date"))

        if (is_movie_name_filled == False) | (is_review_filled == False) | (is_date_filled == False):
            flash("All fields must not be empty.")
            return redirect(url_for("add_movie"))
        elif (is_movie_name_length_validated == False):
            flash("Movie name must be 1-50 characters.")
            return redirect(url_for("add_movie"))
        elif (is_movie_review_length_validated == False):
            flash("Movie review must be 1-200 characters.")
            return redirect(url_for("add_movie"))
        elif (is_date_format_validated == False):
            flash("Incorrect data format, should be YYYY-MM-DD")
            return redirect(url_for("add_movie"))
        elif (is_date_entry_validated == False):
            flash("View date cannot be in the future or beyond a 100 years ago.")
            return redirect(url_for("add_movie"))
        else: 
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

@app.route("/delete-movie/<int:movie_id>")
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("my_movies"))

@app.route("/edit-movie/<int:movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    form = EditMovieForm()
    form.movie_review.data = movie.movie_review
    form.view_date.data = movie.view_date

    if request.method == "POST":
        is_review_filled = check_for_empty_field(request.form.get("movie_review"))
        is_date_filled = check_for_empty_field(request.form.get("view_date"))
        is_movie_review_length_validated = check_input_length((request.form.get("movie_review")),1,200)
        is_date_format_validated = check_date_format(request.form.get("view_date"))
        is_date_entry_validated = check_date_entry(request.form.get("view_date"))

        if (is_review_filled == False) | (is_date_filled == False):
            flash("All fields must not be empty.")
            return redirect(url_for('edit_movie', movie_id=movie.id))
        elif (is_movie_review_length_validated == False):
            flash("Movie review must be 1-200 characters.")
            return redirect(url_for('edit_movie', movie_id=movie.id))
        elif (is_date_format_validated == False):
            flash("Incorrect data format, should be YYYY-MM-DD")
            return redirect(url_for('edit_movie', movie_id=movie.id))
        elif (is_date_entry_validated == False):
            flash("View date cannot be in the future or beyond a 100 years ago.")
            return redirect(url_for('edit_movie', movie_id=movie.id))
        else: 
            movie.movie_review=request.form.get("movie_review"),
            movie.view_date=request.form.get("view_date"),
            db.session.commit()
            return redirect(url_for("my_movies"))

    return render_template("/pages/editMoviePage.html",title='Edit Movie', form=form, movie=movie)

@app.route("/community", methods=("GET", "POST"))
def community():
    if "user" in session:
        movies = list(Movie.query.order_by(Movie.view_date.desc()).all())
        return render_template("/pages/community.html", username=session["user"], movies=movies)

    return render_template("/pages/community.html", title='My Movies', movies=movies)