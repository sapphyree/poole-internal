# models.py

from pydoc import describe
from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Wiki_(db.Model):
    wikiid = db.Column(db.Integer, primary_key=True) 
    title=db.Column(db.String(100))
    image=db.Column(db.String(100))
    description=db.Column(db.String(10000))
