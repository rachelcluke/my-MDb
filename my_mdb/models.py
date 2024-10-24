"""This file contains the Postgres Database tables and the Flask Forms."""

from my_mdb import db, app
from flask_login import UserMixin, login_user, LoginManager, \
    login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, \
    SubmitField, DateField, TextAreaField, datetime
from wtforms.validators import InputRequired, Length, ValidationError
import _datetime

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    """Get User ID."""
    return User.query.get(int(user_id))


class User(db.Model):
    """User Class contains id, username, password, db relationship with Movies."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    movies = db.relationship('Movie', backref='User', cascade="all, delete", lazy='dynamic',
                            primaryjoin="User.id == Movie.user_id")

    def __repr__(self):
        """Magic Method to return id, username and password."""
        return self.id, self.username, self.password


class Movie(db.Model):
    """Movie Class contains id, movie_name, movie_review, view_date and relational user_id."""

    id = db.Column(db.Integer,  unique=True, primary_key=True)
    movie_name = db.Column(db.String(50), nullable=False)
    movie_review = db.Column(db.Text, nullable=False)
    view_date = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        """Magic Method to return id, movie_name and user_id."""
        return self.id, self.movie_name, self.user_id


class RegisterForm(FlaskForm):
    """Register Flask Form with inputs: username, password, submit to register new users."""

    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=15)], render_kw={"placeholder": "New Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "New Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        """Validate username field.

        This checks if the username already exists.

        Args:
            string (username): Inputted username.

        """
        existing_user_username = User.query.filter_by(
            username=username.data).first()

        if existing_user_username:
            raise ValidationError(
                'Sorry this username already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    """Post existing user request.

    This is the login authentication form.

    Args:
        username (str): Inputted username.
        password (password): Inputted username.
        submit (submit): Post method.
    """

    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=15)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


class AddMovieForm(FlaskForm):
    """Add Movie Flask Form with inputs: movie_name, movie_review, view_date and submit."""

    movie_name = StringField(validators=[
                           InputRequired(), Length(min=1, max=50)], render_kw={"placeholder": "Movie Name"})

    movie_review = TextAreaField(validators=[
                             InputRequired(), Length(min=1, max=200)], render_kw={"placeholder": "What did you think of the movie? (Max: 200 characers)"})

    view_date = DateField('Date', format='%Y-%m-%d', default=_datetime.date.today())

    submit = SubmitField('Save to My Movies')


class EditMovieForm(FlaskForm):
    """Edit Movie Flask Form with inputs: movie_review, view_date and submit."""

    movie_review = TextAreaField(validators=[
                             InputRequired(), Length(min=1, max=200)])

    view_date = DateField('Date', format='%Y-%m-%d', default=_datetime.date.today())

    submit = SubmitField('Update my Movie Entry')
