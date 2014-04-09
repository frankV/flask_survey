from flask.ext.wtf import Form, fields, validators
from flask.ext.wtf import Required, Email, ValidationError
from models import User
from app import db

def validate_login(form, field):
    user = form.get_user()

    if user is None:
        raise validators.ValidationError('Invalid user')

    if user.password != form.password.data:
        raise validators.ValidationError('Invalid password')


class LoginForm(Form):
    name = fields.TextField(validators=[Required()])
    password = fields.PasswordField(validators=[Required(), validate_login])

    def get_user(self):
        return db.session.query(User).filter_by(name=self.name.data).first()


class RegistrationForm(Form):
    name = fields.TextField(validators=[Required()])
    email = fields.TextField(validators=[Email()])
    password = fields.PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = fields.PasswordField(validators=[Required()])

    def validate_name(self, field):
        if db.session.query(User).filter_by(name=self.name.data).count() > 0:
            raise validators.ValidationError('Duplicate name')

    def validate_email(self, field):
        if db.session.query(User).filter_by(email=self.email.data).count() > 0:
            raise validators.ValidationError('Duplicate email')

# from flask.ext.wtf import Form
# from wtforms import TextField, BooleanField, TextAreaField
# from wtforms.validators import Required, Length

# class LoginForm(Form):
# 	username = TextField('username', validators = [Required()])
# 	passwd = TextField('passwd', validators = [Required()])
# 	# openid = TextField('openid', validators = [Required()])
# 	# remember_me = BooleanField('remember_me', default = False)

# class CreateAcctForm(Form):
# 	username = TextField('username', validators = [Required()])
# 	passwd = TextField('passwd', validators = [Required()])

# 	def validate(self):
# 		if not Form.validate(self):
# 			return False
# 		if self.username.data == self.original_username:
# 			return True
# 		user = User.query.filter_by(username = self.username.data).first()
# 		if user != None:
# 			self.username.errors.append('This email is already in use. Please choose another one.')
# 			return False
# 		return True


# # class EditForm(Form):
# #     nickname = TextField('nickname', validators = [Required()])
# #     about_me = TextAreaField('about_me', validators = [Length(min = 0, max = 140)])
    
# #     def __init__(self, original_nickname, *args, **kwargs):
# #         Form.__init__(self, *args, **kwargs)
# #         self.original_nickname = original_nickname
        
# #     def validate(self):
# #         if not Form.validate(self):
# #             return False
# #         if self.nickname.data == self.original_nickname:
# #             return True
# #         user = User.query.filter_by(nickname = self.nickname.data).first()
# #         if user != None:
# #             self.nickname.errors.append('This nickname is already in use. Please choose another one.')
# #             return False
# #         return True
