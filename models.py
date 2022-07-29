from ctypes import sizeof
from flask import appcontext_pushed
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Bike(db.Model):
    __tablename__ = 'bikes'

    id =db.Column(db.Integer,
        primary_key = True,
        autoincrement = True)
    
    name =db.Column(db.String,
        nullable = False,
        unique = True)
    
    price = db.Column(db.Float,
        nullable = False,
        unique = False)

    color = db.Column(db.String,
        nullable = False,
        unique = False)
    
    size = db.Column(db.Float,
        nullable = False,
        unique = False)
    
    description = db.Column(db.String,
        nullable = False,
        unique = False)

    image_url = db.Column(db.String,
        nullable = False,
        unique = True)