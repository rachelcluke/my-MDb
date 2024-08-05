from wtforms import StringField, PasswordField, DateField, IntegerField, BooleanField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, EqualTo, Email, Regexp, Optional
import email_validator
from flask_login import current_user
from wtforms import ValidationError, validators
from models import MyMDB_User


class login_form(FlaskForm):
    email = StringField(validators=[InputRequired(), Email(), Length(min=1, max=64)])
    pwd = PasswordField(validators=[InputRequired(), Length(min=8, max=25)])
    username = StringField(validators=[Optional()])

class signup_form(FlaskForm):
    username = StringField(
        validators=[
            InputRequired(),
            Length(5, 20, message="Please provide a valid username."),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Usernames must have only letters, numbers, dots or underscores",
            ),
        ]
    )
    email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    pwd = PasswordField(validators=[InputRequired(), Length(8, 72)])

    #Validations
    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("This Email has already been registered.")

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError("Username already taken, please choose another.")