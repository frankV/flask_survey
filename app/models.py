from mixins import CRUDMixin
from flask.ext.login import UserMixin
from flask.ext.sqlalchemy import SQLAlchemy
from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(UserMixin, CRUDMixin,  db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), unique = True)
    password = db.Column(db.String(20))
    oldPassword = db.Column(db.String(20))
    s1 = db.Column(db.Boolean)
    s2 = db.Column(db.Boolean)
    s3 = db.Column(db.Boolean)
    s4 = db.Column(db.Boolean)
    lastSeen = db.Column(db.DateTime)
    
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    db = db.relationship('Database', backref='user', lazy='dynamic')

    def __init__(self, name=None, password=None, oldPassword = None, s1=False, s2=False, s3=False, s4=False):
        self.name = name
        self.password = password
        self.oldPassword = oldPassword
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4

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
        return '<User %r>' % (self.name)

class Database(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    survey1_id = db.Column(db.Integer, db.ForeignKey('survey1.id'))
    survey2_id = db.Column(db.Integer, db.ForeignKey('survey2.id'))
    survey3_id = db.Column(db.Integer, db.ForeignKey('survey3.id'))
    survey4_id = db.Column(db.Integer, db.ForeignKey('survey4.id'))

    name = db.Column(db.String(255), unique = True)

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<Database %r>' % (self.name)

class Survey1(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    gender = db.Column(db.String)
    age = db.Column(db.String)
    education = db.Column(db.String)
    language = db.Column(db.String(20))
    db = db.relationship('Database', backref='survey1', lazy='dynamic')

    def __init__(self, gender=None, age=None, education=None, language=None):
        self.gender=gender
        self.age=age
        self.education=education
        self.language=language

    def get_id(self):
        return unicode(self.id)

    # def __repr__(self):
    #     return '<Survey1 %r>' % (self.gender)

class Survey2(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    major = db.Column(db.String)
    department = db.Column(db.String(30))
    count = db.Column(db.String)
    unique = db.Column(db.String)
    db = db.relationship('Database', backref='survey2', lazy='dynamic')

    def __init__(self, major=None, department=None, count=None, unique=None):
        self.major=major
        self.department=department
        self.count=count
        self.unique=unique

    def get_id(self):
        return unicode(self.id)

class Survey3(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    choose = db.Column(db.String)
    secure = db.Column(db.String)
    modify = db.Column(db.String)
    usedPassword = db.Column(db.String)
    wordPart = db.Column(db.String)
    numberPart = db.Column(db.String)
    charPart = db.Column(db.String)
    db = db.relationship('Database', backref='survey3', lazy='dynamic')

    def __init__(self, choose=None, secure=None, modify=None, usedPassword=None, wordPart=None, numberPart=None, charPart=None,):
        self.choose=choose
        self.secure=secure
        self.modify=modify
        self.usedPassword=usedPassword
        self.wordPart=wordPart
        self.numberPart=numberPart
        self.charPart=charPart

    def get_id(self):
        return unicode(self.id)

class ChooseSelectMultiple(db.Model):
    id = db.Column(db.Integer, primary_key = True)
        

class Survey4(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    computerTime = db.Column(db.String)
    passwordCreation = db.Column(db.String)
    storePasswords = db.Column(db.String)
    howStored = db.Column(db.String)
    comments = db.Column(db.String)

    def __init__(self, computerTime=None, passwordCreation=None, storePasswords=None, howStored=None, comments=None):
        self.computerTime=computerTime
        self.passwordCreation=passwordCreation
        self.storePasswords=storePasswords
        self.howStored=howStored
        self.comments=comments

    def get_id(self):
        return unicode(self.id)