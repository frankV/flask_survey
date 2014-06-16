from mixins import CRUDMixin
from flask.ext.login import UserMixin
from flask.ext.sqlalchemy import SQLAlchemy
from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(UserMixin, CRUDMixin,  db.Model):

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(20), unique = True)
    password = db.Column(db.String(20))
    oldPassword = db.Column(db.String(20))
    s1 = db.Column(db.Boolean)
    s2 = db.Column(db.Boolean)
    s3 = db.Column(db.Boolean)
    s4 = db.Column(db.Boolean)
    lastSeen = db.Column(db.String)
    
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    db = db.relationship('Database', backref='user', lazy='dynamic')

    def __init__(self, email=None, password=None, oldPassword = None, s1=False, s2=False, s3=False, s4=False):
        self.email = email
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
        return '<User %r>' % (self.email)

class Database(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    survey1_id = db.Column(db.Integer, db.ForeignKey('survey1.id'))
    survey2_id = db.Column(db.Integer, db.ForeignKey('survey2.id'))
    survey3_id = db.Column(db.Integer, db.ForeignKey('survey3.id'))
    survey4_id = db.Column(db.Integer, db.ForeignKey('survey4.id'))

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<Database %r>' % (self.id)

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
    choose = db.relationship('ChooseSelectMultiple', backref='survey3', lazy='dynamic')
    secure = db.relationship('SecureSelectMultiple', backref='survey3', lazy='dynamic')
    modify = db.Column(db.String)
    usedPassword = db.Column(db.String)
    wordPart = db.Column(db.String)
    numberPart = db.relationship('NumberPartSelectMultiple', backref='survey3', lazy='dynamic')
    charPart = db.relationship('CharPartSelectMultiple', backref='survey3', lazy='dynamic')
    db = db.relationship('Database', backref='survey3', lazy='dynamic')

    def __init__(self, modify=None, usedPassword=None, wordPart=None):
        self.modify=modify
        self.wordPart=wordPart
        self.usedPassword=usedPassword

    def get_id(self):
        return unicode(self.id)

class CharPartSelectMultiple(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    N = db.Column(db.String)
    added_symbols = db.Column(db.String)
    deleted_symbols = db.Column(db.String)
    substituted_symbols = db.Column(db.String)
    O = db.Column(db.String)
    survey3_id = db.Column(db.Integer, db.ForeignKey('survey3.id'))

    def __init__(self, N=None, added_symbols=None, deleted_symbols=None, substituted_symbols=None, O=None):
        self.N = N
        self.added_symbols = added_symbols
        self.deleted_symbols = deleted_symbols
        self.substituted_symbols = substituted_symbols
        self.O = O

    def get_id(self):
        return unicode(self.id)

class NumberPartSelectMultiple(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    N = db.Column(db.String)
    added_digits = db.Column(db.String)
    deleted_digits = db.Column(db.String)
    substituted_digits = db.Column(db.String)
    O = db.Column(db.String)
    survey3_id = db.Column(db.Integer, db.ForeignKey('survey3.id'))

    def __init__(self, N=None, added_digits=None, deleted_digits=None, substituted_digits=None, O=None):
        self.N = N
        self.added_digits = added_digits
        self.deleted_digits = deleted_digits
        self.substituted_digits = substituted_digits
        self.O = O

    def get_id(self):
        return unicode(self.id)

class SecureSelectMultiple(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    numbers = db.Column(db.String)
    upper_case = db.Column(db.String)
    symbols = db.Column(db.String)
    eight_chars = db.Column(db.String)
    no_dict = db.Column(db.String)
    adjacent = db.Column(db.String)
    nothing = db.Column(db.String)
    survey3_id = db.Column(db.Integer, db.ForeignKey('survey3.id'))

    def __init__(self, numbers=None, upper_case=None, symbols=None, eight_chars=None, no_dict=None, adjacent=None, nothing=None):
        self.numbers = numbers
        self.upper_case = upper_case
        self.symbols = symbols
        self.eight_chars = eight_chars
        self.no_dict = no_dict
        self.adjacent = adjacent
        self.nothing=nothing

    def get_id(self):
        return unicode(self.id)   
class ChooseSelectMultiple(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    names = db.Column(db.String)
    numbers = db.Column(db.String)
    songs = db.Column(db.String)
    mnemonic = db.Column(db.String)
    sports = db.Column(db.String)
    famous = db.Column(db.String)
    words = db.Column(db.String)
    survey3_id = db.Column(db.Integer, db.ForeignKey('survey3.id'))

    def __init__(self, names=None, numbers=None, song=None, mnemonic=None, sports=None, famous=None, words=None):
        self.names = names
        self.numbers = numbers
        self.song = song
        self.mnemonic = mnemonic
        self.sports = sports
        self.famous = famous
        self.words = words

    def get_id(self):
        return unicode(self.id)

class Survey4(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    computerTime = db.Column(db.String)
    passwordCreation = db.relationship('PasswordCreationSelectMultiple', backref='survey4', lazy='dynamic')
    howStored = db.Column(db.String)
    comments = db.Column(db.String)

    def __init__(self, computerTime=None, howStored=None, comments=None):
        self.computerTime=computerTime
        self.howStored=howStored
        self.comments=comments

    def get_id(self):
        return unicode(self.id)
class HowStoredSelectMultiple(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    regular_file = db.Column(db.String)
    encrypted = db.Column(db.String)
    software = db.Column(db.String)
    cellphone = db.Column(db.String)
    browser = db.Column(db.String)
    write_down = db.Column(db.String)
    no = db.Column(db.String)
    survey4_id = db.Column(db.Integer, db.ForeignKey('survey4.id'))

    def __init__(self, regular_file=None, encrypted=None, software=None, cellphone=None, browser=None, write_down=None, no=None):
        self.regular_file = regular_file
        self.encrypted = encrypted
        self.software = software
        self.cellphone = cellphone
        self.browser = browser
        self.write_down = write_down
        self.no = no

    def get_id(self):
        return unicode(self.id)

class PasswordCreationSelectMultiple(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    random = db.Column(db.String)
    reuse = db.Column(db.String)
    modify = db.Column(db.String)
    new = db.Column(db.String)
    substitute = db.Column(db.String)
    multiword = db.Column(db.String)
    phrase = db.Column(db.String)
    O = db.Column(db.String)
    survey4_id = db.Column(db.Integer, db.ForeignKey('survey4.id'))

    def __init__(self, random=None, reuse=None, modify=None, new=None, substitute=None, multiword=None, phrase=None, O=None):
        self.random = random
        self.reuse = reuse
        self.modify = modify
        self.new = new
        self.substitute = substitute
        self.multiword = multiword
        self.phrase = phrase
        self.O = O

    def get_id(self):
        return unicode(self.id)
        