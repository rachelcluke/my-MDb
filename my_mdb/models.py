from my_mdb import db
from flask_login import UserMixin
from flask_wtf import wtforms
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

#user model
class User(db.Model):
   # __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    pwd = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return  self.id, self.username, self.pwd
