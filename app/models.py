from app import db
from hashlib import md5

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(64), index=True, unique=True)
	amount = db.Column(db.Integer)
	contrib = db.relationship('Contributions', backref="contributor", lazy='dynamic')

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.id)
		except NameError:
			return str(self.id)

	def __repr__(self):
		return '<User ' + str(self.name) + " amount: " + str(self.amount) + " id:" + str(self.id) + " email:" + str(self.email) + ">"

class Contributions(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	date = db.Column(db.DateTime)
	amount = db.Column(db.Integer)
	name = db.Column(db.String(64))
	cat = db.Column(db.String(64))

	def __repr__(self):
		return '<Contribution %r>' % (self.amount)