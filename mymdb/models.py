"""
from mymdb import db
from flask_login import UserMixin

#user model
class MyMDB_User(UserMixin, db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwd = db.Column(db.String(300), unique=True, nullable=False)

    def __repr__(self):
        return '<MyMDB_User %r>' % self.username
"""