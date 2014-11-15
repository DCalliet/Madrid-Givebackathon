from app import db
from hashlib import md5

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(64), index=True, unique=True)
	amount = db.Column(db.Integer)
