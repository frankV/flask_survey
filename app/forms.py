from flask.ext.wtf import Form, fields, validators, Required, Email, ValidationError, Length
from wtforms import widgets
from models import User
from app import db

def validate_login(form, field):
    user = form.get_user()
    
    if user is None:
        raise validators.ValidationError('Invalid user')

    if user.password != form.password.data:
        raise validators.ValidationError('Invalid password')

class LoginForm(Form):
    email = fields.TextField(validators=[Required(), Email()])
    password = fields.PasswordField(validators=[Required(), validate_login])

    def get_user(self):
        return db.session.query(User).filter_by(email=self.email.data).first()

class ForgotPasswordForm(Form):
    email = fields.TextField(validators=[Required(), Email()])

    def get_user(self):
        return db.session.query(User).filter_by(email=self.email.data).first()

class RegistrationForm(Form):
    email = fields.TextField('Email Address', validators=[Required(), Email()])
    consent = fields.BooleanField(validators=[Required()])
    password = fields.PasswordField('New Password', [
        validators.Required(), validators.Length(min=8, max=20),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = fields.PasswordField(validators=[Required()])

    def validate_email(self, field):
        if db.session.query(User).filter_by(email=self.email.data).count() > 0:
            raise validators.ValidationError('Duplicate email')

class NewPass(Form):
    password = fields.PasswordField('New Password', [
        validators.Required(), validators.Length(min=8, max=20),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = fields.PasswordField(validators=[Required()])    

    # def validate_new_pass(self, field):
    #     if db.session.query(User).filter_by(password=self.name.data).count() > 0:   #NOT SURE IF CORRECT
    #         raise validators.ValidationError('Duplicate Password')

class Survey1Form(Form):
    gender = fields.RadioField('What is your gender?', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], validators = [Required()])
    age = fields.RadioField('What is your age?', choices=[('lt18', 'Younger than 18'), ('18-24', '18 to 24'), ('25-34', '25 to 34'), 
        ('35-44', '35 to 44'), ('45-54', '45 to 54'), ('55-64', '55 to 64'), ('65-74', '65 to 74'), ('75oa', '75 or above')], validators=[Required()])
    education = fields.RadioField('Which of the following best describes your highest education level?', choices=[('Hsg', 'High school graduate'), 
        ('Scnd', 'Some college, no degree'), ('Assoc', 'Associates Degree'), ('Bach', 'Bachelors degree'), ('Grad', 'Graduate degree (Masters, Doctorate, etc.)'), ('O', 'Other')], 
        validators=[Required()])
    language = fields.TextField('Native Language', validators=[Required()])

class Survey2Form(Form):
    major = fields.RadioField('Are you majoring in or do you have a degree or job in computer science, computer engineering, information technology, or a related field?', 
        choices=[('Y', 'yes'), ('N', 'No'), ('O','I prefer not to answer')], validators = [Required()])
    department = fields.TextField('In what department are you majoring?', validators=[Required()])
    count = fields.RadioField('How many website user-names and passwords do you have, approximately?', choices=[('lt5', 'Less than 5 accounts'), 
        ('5-10', '5 to 10 Accounts'), ('11-20', '11 to 20 Accounts'), ('gt20', 'More Than 20 Accounts') ])
    unique = fields.RadioField('Do you try to create unique passwords for each different account?', choices=[
        ('Y', 'Yes, I create a new password every time I create a new account or every time I have to change my password'), 
        ('N', 'No, I use my old passwords that I have already created for my other accounts'), 
        ('O', 'I mostly create a new password, but sometimes use old passwords')], validators=[Required()])

class Survey3Form(Form):
    choose = fields.SelectMultipleField('How did you choose your new password? Were you influenced by any of the following? (Please check all that apply.)', 
        choices = [('names', 'Names of family members, relatives, close friends'), ('numbers', 'Familiar numbers (birth date, telephone number, street address, employee number, etc.)'),
        ('songs', 'Songs, movies, television shows, books, poetry or games'), ('mnemonic', 'Scientific or other educational mnemonics'), 
        ('sports', 'Sports teams and players'), ('famous', 'Names of famous people or characters'), ('words', 'Words in a language other than English')], 
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False))
    secure = fields.SelectMultipleField('When creating your new password, did you consider any of the following policies to make your password more secure? (Please check all that apply.)', 
        choices = [('numbers', 'Include numbers'), ('upper_case', 'Include upper case letters'), ('symbols', 'Include symbols'), 
        ('eight_chars', 'Have 8 or more characters'), ('no_dict', 'Not contain dictionary words'), 
        ('adjacent', 'Not containing a sequence of adjacent or repeated characters on your keyboard (e.g. qwerty)'), 
        ('nothing', 'I did not consider any policy')],
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False))
    modify = fields.RadioField('Did you create your new password by slightly changing your old password for this website?', choices=[
        ('Y', 'Yes'), ('N', 'No')], validators=[Required()])
    usedPassword = fields.RadioField('Is the password that you have just created one that you have used in the past?', choices=[
        ('Y', 'Yes'), ('N', 'No'), ('O', 'Password has similarities to another password that I have used before')], validators=[Required()])
    wordPart = fields.RadioField('If you created your new password based on one of your old passwords, did you consider changing the word part in one of the following ways?',
        choices=[('N', 'Not applicable'), ('Changed_completely', 'Changed completely'), ('Changed_slightly', 'Changed slightly'), 
        ('Capitalized_letters', 'Capitalized letters'), ('O', 'Other')], validators=[Required()])
    numberPart = fields.SelectMultipleField('If you created your new password based on one of your old passwords, did you consider changing the number part in one of the following ways?', 
        choices=[('N', 'Not applicable'), ('added_digits', 'Added digits'), ('deleted_digits', 'Deleted digits'), ('substituted_digits', 'Substituted digits'), 
        ('O', 'Other')], validators=[Required()], 
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False))
    charPart = fields.SelectMultipleField('If you created your new password based on one of your old passwords, did you consider changing the special character part in one of the following ways?', 
        choices=[('N', 'Not applicable'), ('added_symbols', 'Added symbols'), ('deleted_symbols', 'Deleted symbols'), ('substituted_symbols', 'Substituted symbols'),
        ('O', 'Other')], validators=[Required()], 
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False))

class Survey4Form(Form):
    computerTime = fields.RadioField('How long have you been using a computer?', choices=[
        ('0-2', '0 to 2 Years'), ('3-5', '3 to 5 Years'), ('6-10', '6 to 10 Years'), ('mt10', 'More than 10 years')], validators=[Required()])
    passwordCreation = fields.SelectMultipleField('How do you usually create passwords for your accounts? (Please check all that apply.)', choices=[
        ('random', 'Randomly generate a password using special software or apps'), ('reuse', 'Reuse a password that is used for another account'),
        ('modify', 'Modify a password that is used for another account'), ('new', 'Create a new password using a familiar number or a name of a family member'),
        ('substitute', 'Choose a word and substitute some letters with numbers of symbols (for example @ for a)'), 
        ('multiword', 'Use a pass-phrase consisting of several words'), ('phrase', 'Choose a phrase and use the first letters of each word'),('O', 'Other')], 
        validators=[Required()], 
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False))
    howStored = fields.SelectMultipleField('Do you store your passwords? If yes how? (Check all that apply.)', 
        choices=[('regular_file', 'I store my passwords in a regular file / document on my computer.'), 
        ('encrypted', 'I store my passwords in an encrypted computer file'), ('software', 'I use password management software to securely store my passwords'),
        ('cellphone', 'I store my passwords on my cellphone / smartphone'), ('browser', 'I save my passwords in the browser'), 
        ('write_down', 'I write down my password on a piece of paper'), ('no', 'No, I do not save my passwords. I remember them.')], 
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False))
    comments = fields.TextAreaField('If you have any additional feedback about passwords or this survey, please enter your comments here.')
