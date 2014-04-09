# from hashlib import md5
from mixins import CRUDMixin
from flask.ext.login import UserMixin
from flask.ext.sqlalchemy import SQLAlchemy
from app import db
# import flask.ext.whooshalchemy as whooshalchemy

ROLE_USER = 0
ROLE_ADMIN = 1

class User(UserMixin, CRUDMixin,  db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(120))
    
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    db = db.relationship('Database', backref='user', lazy='dynamic')

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.password = password

    def is_active(self):
        return True

    def get_id(self):
        return unicode(self.id)

    def is_admin(self):
        if self.role > 0:
            return True
        else:
            return False

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Database(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(255), unique = True)

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '%r' % (self.name)

# class User(db.Model):
# 	__tablename__ = "users"
# 	id = db.Column('user_id', db.Integer, primary_key = True)
# 	username = db.Column('username', db.String(64), index = True, unique = True)
# 	passwd = db.Column('passwd',db.String(20), index = True)
# 	role = db.Column('role', db.SmallInteger, default = ROLE_USER)
# 	registered_on = db.Column('registered_on' , db.DateTime)
# 	surveys = db.relationship('Survey', backref = 'author', lazy='dynamic')	#db.relationship is a many to 1, probably wont use for finished product
	
# 	def __init__(self, username, passwd, role):
# 		self.username = username
# 		self.passwd = passwd
# 		self.role = role
# 		self.registered_on = datetime.estnow()

# 	def is_authenticated(self):
# 		return True

# 	def is_active(self):
# 		return True

# 	def is_anonymous(self):
# 		return False

# 	def get_id(self):
# 		return unicode(self.id)

# 	def __repr__(self):				#printing, for purposes of debugging
# 		return '<User %r>' % (self.username)

# class Survey(db.Model):
# 	id = db.Column(db.Integer, primary_key = True)
#     	body = db.Column(db.String(140))
#     	timestamp = db.Column(db.DateTime)
#     	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# 	def __repr__(self):
# 		return '<Survey %r>' % (self.body)

