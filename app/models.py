# from hashlib import md5
from app import db
# from app import app
# import flask.ext.whooshalchemy as whooshalchemy

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
	__tablename__ = "users"
	id = db.Column('user_id', db.Integer, primary_key = True)
	username = db.Column('username', db.String(64), index = True, unique = True)
	passwd = db.Column('passwd',db.String(20), index = True)
	role = db.Column('role', db.SmallInteger, default = ROLE_USER)
	surveys = db.relationship('Survey', backref = 'author', lazy='dynamic')	#db.relationship is a many to 1, probably wont use for finished product
	
	def __init__(self, username, passwd, role):
		self.username = username
		self.passwd = passwd
		self.role = role

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):				#printing, for purposes of debugging
		return '<User %r>' % (self.username)

class Survey(db.Model):
	id = db.Column(db.Integer, primary_key = True)
    	body = db.Column(db.String(140))
    	timestamp = db.Column(db.DateTime)
    	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Survey %r>' % (self.body)

