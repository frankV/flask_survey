from mixins import CRUDMixin
from flask.ext.login import UserMixin
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref

from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(UserMixin, CRUDMixin,  db.Model):
    # __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True, unique=True)
    userid = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique = True)
    password = db.Column(db.String(20))
    oldPassword = db.Column(db.String(20))
    changedPass = db.Column(db.Boolean)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    s1 = db.Column(db.Boolean)
    s2 = db.Column(db.Boolean)
    s3 = db.Column(db.Boolean)
    s4 = db.Column(db.Boolean)
    lastSeen = db.Column(db.String(255))
    survey1 = db.relationship('Survey1', backref=db.backref('user', lazy='joined'))
    survey2 = db.relationship('Survey2', backref=db.backref('user', lazy='joined'))
    survey3 = db.relationship('Survey3', backref=db.backref('user', lazy='joined'))
    survey4 = db.relationship('Survey4', backref=db.backref('user', lazy='joined'))

    def __init__(self, email=None, userid=None, password=None, oldPassword = None, changedPass=False,
        s1=False, s2=False, s3=False, s4=False, role=None):
        self.email = email
        self.userid = userid
        self.password = password
        self.oldPassword = oldPassword
        self.changedPass = changedPass
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4
        self.role=role

    def is_admin(self):
        if self.role == 1:
            return True
        else:
            return False

    def is_active(self):
        return True

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.email)


class Survey1(db.Model):
    # __tablename__='survey1'
    id = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    age = db.Column(db.String(255))
    education = db.Column(db.String(255))
    language = db.Column(db.String(20))
    userid = db.Column(db.String(255), db.ForeignKey('user.userid'))
    #user = db.relationship('User', backref=db.backref('survey1', lazy='dynamic'))

    def __init__(self, gender=None,age=None, education=None, language=None, userid=None):
        self.gender=gender
        self.age=age
        self.education=education
        self.language=language
        self.userid = userid

    def get_id(self):
        return unicode(self.id)


class Survey2(db.Model):
    # __tablename__='survey2'
    id = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.String(255))
    major = db.Column(db.String(255))
    department = db.Column(db.String(30))
    count = db.Column(db.String(255))
    unique = db.Column(db.String(255))
    userid = db.Column(db.String(255), db.ForeignKey('user.userid'))
    # user = db.relationship('User', backref=db.backref('survey2', lazy='dynamic'))

    def __init__(self, major=None, department=None, count=None, unique=None, userid=None):
        self.major=major
        # self.department=department
        self.count=count
        self.unique=unique
        self.userid=userid

    def get_id(self):
        return unicode(self.id)

class Survey3(db.Model):
    # __tablename__='survey3'
    id = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.String(255))
    choose_names = db.Column(db.Boolean)
    choose_numbers = db.Column(db.Boolean)
    choose_songs = db.Column(db.Boolean)
    choose_mnemonic = db.Column(db.Boolean)
    choose_sports = db.Column(db.Boolean)
    choose_famous = db.Column(db.Boolean)
    choose_words = db.Column(db.Boolean)
    choose_other=db.Column(db.Boolean)
    specify=db.Column(db.String(255))
    secure_numbers = db.Column(db.Boolean)
    secure_upper_case = db.Column(db.Boolean)
    secure_symbols = db.Column(db.Boolean)
    secure_eight_chars = db.Column(db.Boolean)
    secure_no_dict = db.Column(db.Boolean)
    secure_adjacent = db.Column(db.Boolean)
    secure_nothing = db.Column(db.Boolean)
    secure_other=db.Column(db.Boolean)
    specify1=db.Column(db.String(255))
    modify = db.Column(db.String(255))
    usedPassword = db.Column(db.String(255))
    wordPart = db.Column(db.String(255))
    number_N = db.Column(db.Boolean)
    number_changed_slightly=db.Column(db.Boolean)
    number_changed_completely=db.Column(db.Boolean)
    number_added_digits = db.Column(db.Boolean)
    number_deleted_digits = db.Column(db.Boolean)
    number_substituted_digits = db.Column(db.Boolean)
    number_O = db.Column(db.String(255))
    char_N = db.Column(db.Boolean)
    char_changed_slightly=db.Column(db.Boolean)
    char_changed_completly=db.Column(db.Boolean)
    char_added_symbols = db.Column(db.Boolean)
    char_deleted_symbols = db.Column(db.Boolean)
    char_substituted_symbols = db.Column(db.Boolean)
    char_O = db.Column(db.String(255))
    userid = db.Column(db.String(255), db.ForeignKey('user.userid'))
    # user = db.relationship('User', backref=db.backref('survey3', lazy='dynamic'))

    def __init__(self, choose_names=None, choose_numbers=None, choose_songs=None,
        choose_mnemonic=None, choose_sports=None, choose_famous=None, choose_words=None,
        secure_numbers=None, secure_upper_case=None, secure_symbols=None,
        secure_eight_chars=None, secure_no_dict=None, secure_adjacent=None, secure_nothing=None,
        modify=None, usedPassword=None, wordPart=None, number_N=None, number_added_digits=None,
        number_deleted_digits=None, number_substituted_digits=None, number_O=None,
        char_N=None, char_added_symbols=None, char_deleted_symbols=None,
        char_substituted_symbols=None, char_O=None, userid=None,choose_other=None,specify=None,specify1=None,secure_other=None,number_changed_completly=None,number_changed_slightly=None,char_changed_slightly=None,char_changed_completly=None):

        self.choose_names=choose_names
        self.choose_numbers=choose_numbers
        self.choose_songs=choose_songs
        self.choose_mnemonic=choose_mnemonic
        self.choose_sports=choose_sports
        self.choose_famous=choose_famous
        self.choose_words=choose_words
        self.choose_other=choose_other
        self.specify=specify
        self.secure_numbers=secure_numbers
        self.secure_upper_case=secure_upper_case
        self.secure_symbols=secure_symbols
        self.secure_eight_chars=secure_eight_chars
        self.secure_no_dict=secure_no_dict
        self.secure_adjacent=secure_adjacent
        self.secure_nothing=secure_nothing
        self.secure_other=secure_other
        self.specify1=specify1
        self.modify=modify
        self.usedPassword=usedPassword
        self.wordPart=wordPart
        self.number_N=number_N
        self.number_changed_slightly=number_changed_slightly
        self.number_changed_completly=number_changed_completly
        self.number_added_digits=number_added_digits
        self.number_deleted_digits=number_deleted_digits
        self.number_substituted_digits=number_substituted_digits
        self.number_O=number_O
        self.char_N=char_N
        self.char_changed_slightly=char_changed_slightly
        self.char_changed_completly=char_changed_completly
        self.char_added_symbols=char_added_symbols
        self.char_deleted_symbols=char_deleted_symbols
        self.char_substituted_symbols=char_substituted_symbols
        self.char_O=char_O
        self.userid=userid

    def get_id(self):
        return unicode(self.id)


class Survey4(db.Model):
    # __tablename__='survey4'
    id = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.String(255))
    computerTime = db.Column(db.String(255))
    pass_random = db.Column(db.Boolean)
    pass_reuse = db.Column(db.Boolean)
    pass_modify = db.Column(db.Boolean)
    pass_new = db.Column(db.Boolean)
    pass_substitute = db.Column(db.Boolean)
    pass_multiword = db.Column(db.Boolean)
    pass_phrase = db.Column(db.Boolean)
    pass_O = db.Column(db.String(255))
    how_regular_file = db.Column(db.Boolean)
    how_encrypted = db.Column(db.Boolean)
    how_software = db.Column(db.Boolean)
    how_cellphone = db.Column(db.Boolean)
    how_browser = db.Column(db.Boolean)
    how_write_down = db.Column(db.Boolean)
    how_no = db.Column(db.Boolean)
    comments = db.Column(db.String(255))
    userid = db.Column(db.String(255), db.ForeignKey('user.userid'))
    # user = db.relationship('User', backref=db.backref('survey4', lazy='dynamic'))

    def __init__(self, computerTime=None, pass_random=None, pass_reuse=None,
        pass_modify=None, pass_new=None, pass_substitute=None, pass_multiword=None,
        pass_phrase=None, pass_O=None, how_regular_file=None, how_encrypted=None,
        how_software=None, how_cellphone=None, how_browser=None, how_write_down=None,
        how_no=None, comments=None, userid=None):

        self.computerTime=computerTime
        self.pass_random = pass_random
        self.pass_reuse = pass_reuse
        self.pass_modify = pass_modify
        self.pass_new = pass_new
        self.pass_substitute = pass_substitute
        self.pass_multiword = pass_multiword
        self.pass_phrase = pass_phrase
        self.pass_O = pass_O
        self.how_regular_file = how_regular_file
        self.how_encrypted = how_encrypted
        self.how_software = how_software
        self.how_cellphone = how_cellphone
        self.how_browser = how_browser
        self.how_write_down = how_write_down
        self.how_no = how_no
        self.comments=comments
        self.userid=userid

    def get_id(self):
        return unicode(self.id)