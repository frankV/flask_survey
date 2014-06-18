#FLASK
from flask import abort, render_template, Response, flash, redirect, session, url_for, g, request, send_from_directory
#FLASK EXTENSIONS
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext.sqlalchemy import get_debug_queries
from flask.ext.mail import Mail
#LOCAL
from models import User, ROLE_USER, ROLE_ADMIN, Survey1, Survey2, Survey3, Survey4, CharPartSelectMultiple, NumberPartSelectMultiple
from models import SecureSelectMultiple, ChooseSelectMultiple, HowStoredSelectMultiple, PasswordCreationSelectMultiple, PasswordCreationSelectMultiple
from forms import LoginForm, RegistrationForm, Survey1Form, Survey2Form, Survey3Form, Survey4Form, NewPass, ForgotPasswordForm
from email import user_notification, forgot_password
from config import DATABASE_QUERY_TIMEOUT
from app import app, db, lm, mail
#OTHER
from  datetime import date, timedelta

# session.permanent = True
# app.permanent_session_lifetime = timedelta(minutes=10)

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.route('/survey_1/', methods=['GET','POST'])
@login_required
def survey_1():
	g.user = current_user
	form = Survey1Form(request.form)
	if form.validate_on_submit():

		g.user.s1=True
		g.user.lastSeen=date.today()
		model = Survey1(gender=form.gender.data, age=form.age.data, education=form.education.data, language=form.language.data)
		
		form.populate_obj(model)
		
		db.session.add(model)		
		db.session.add(g.user)

		db.session.commit()
		logout_user()

		return redirect(url_for('logouthtml'))
	return render_template('Survey1.html', title='Survey', form=form)

@app.route('/survey_2/', methods=['GET','POST'])
@login_required
def survey_2():
	g.user = current_user
	form = Survey2Form(request.form)
	if form.validate_on_submit():
		
		g.user.s2=True
		g.user.lastSeen=date.today()
		model=Survey2(major=form.major.data, department=form.department.data, count=form.count.data, unique=form.unique.data)
		
		form.populate_obj(model)
		
		db.session.add(model)		
		db.session.add(g.user)
		
		db.session.commit()
		logout_user()
		
		return redirect(url_for('logouthtml'))
	return render_template('Survey2.html', title='Survey', form=form)

@app.route('/survey_3/', methods=['GET','POST'])
@login_required
def survey_3():
	g.user = current_user
	form = Survey3Form(request.form)
	# flash(flash_errors)
	if form.validate_on_submit():
		flash("Survey3 Validation message")

		g.user.s3=True
		g.user.lastSeen=date.today()
		model = Survey3(modify=form.modify.data, wordPart = form.wordPart.data, usedPassword=form.usedPassword.data)
		charPart = CharPartSelectMultiple(N=form.N.data, added_symbols = form.added_symbols.data, 
			deleted_symbols=form.deleted_symbols.data, substituted_symbols=form.substituted_symbols.data, 
			O = form.O.data)
		numPart = NumberPartSelectMultiple(N=form.N.data, added_digits=form.added_digits.data, 
			deleted_digits=form.deleted_digits.data, substituted_digits=form.substituted_digits.data, 
			O = form.O.data)
		securePart = SecureSelectMultiple(numbers = form.numbers.data, upper_case=form.upper_case.data, 
			symbols=form.symbols.data, eight_chars = form.eight_chars.data, no_dict=form.no_dict.data, adjacent=form.adjacent.data,
			nothing=form.nothing.data)
		choosePart = PasswordCreationSelectMultiple(names = form.names.data, numbers = form.numbers.data, songs=form.songs.data,
			mnemonic = form.mnemonic.data, sports = form.sports.data, famous=form.famous.data, words=form.words.data)

		form.populate_obj(model)
		form.populate_obj(charPart)
		form.populate_obj(numPart)
		form.populate_obj(securePart)
		form.populate_obj(choosePart)

		db.session.add(g.user)
		db.session.add(model)
		db.session.add(charPart)
		db.session.add(numPart)
		db.session.add(choosePart)
		db.session.add(SecurePart)

		db.session.commit()
		logout_user()

		return redirect(url_for('logouthtml'))
	return render_template('Survey3.html', title='Survey', form=form)

@app.route('/survey_4/', methods=['GET','POST'])
@login_required
def survey_4():
	g.user = current_user
	form = Survey4Form(request.form)
	# flash(flash_errors)
	if form.validate_on_submit():
		flash("Survey4 Validation message")
		
		g.user.s4=True
		g.user.lastSeen=date.today()
		model = Survey4(computerTime=form.computerTime.data, comments=form.comments.data)
		# howStored = HowStoredSelectMultiple(howStored.data
		# 	# regular_file=form.regular_file.data, encrypted=form.encrypted.data, software=form.software.data,
		# 	# cellphone=form.cellphone.data, browser=form.browser.data, write_down=form.write_down.data, no=form.no.data)
		# passwordCreation = PasswordCreationSelectMultiple(random=form.random.data, reuse=form.reuse.data, modify=form.modify.data,
		# 	new=form.new.data, substitute=form.substitute.data, multiword=form.multiword.data, phrase=form.phrase.data, O=form.O.data)
		print form.computerTime
		form.populate_obj(model)
		# form.populate_obj(howStored)
		# form.populate_obj(passwordCreation)

		db.session.add(g.user)
		db.session.add(model)
		# db.session.add(howStored)
		# db.session.add(passwordCreation)
		
		db.session.commit()
		logout_user()
		
		return render_template("final.html", title="Thanks!")
	return render_template('Survey4.html', title='Survey', form=form)

@app.route('/create_acct/' , methods=['GET','POST'])
def create_acct():
	form = RegistrationForm(request.form)
	if form.validate_on_submit():
		print form
		user = User(email=form.email.data, password=form.password.data, oldPassword=form.password.data)
		db.session.add(user)
		db.session.commit()
		login_user(user)
		user_notification(user)
		return redirect(url_for('index'))
	return render_template('create_acct.html', title = "Create Account", form=form)

@app.route('/new_pass/' , methods=['GET','POST'])
def new_pass():
	form = NewPass(request.form)
	if form.validate_on_submit():
		print form
		user = g.user
		user.password = form.password.data
		db.session.add(user)
		db.session.commit()
		flash("Thanks for updating your password!")
		return redirect(url_for('index'))
	return render_template('new_pass.html', title='Update Password', form=form)

@app.route('/login/',methods=['GET','POST'])
def login():
	form = LoginForm(request.form)
	if form.validate_on_submit():
		user = form.get_user()
		login_user(user)
		user = g.user
		flash("Logged in successfully.")
		flash(user.s2)
		flash(user.s3)
		if user.s2 is True and user.s3 is False:
			flash("Redirect to new password")
			return redirect(request.args.get("next") or url_for("new_pass"))
		else:
			return redirect(request.args.get("next") or url_for("index"))
	return render_template('login.html', title = "Login", form=form)

@app.route('/forgot_passwd', methods=['GET', 'POST'])
def forgot_passwd():
	form = ForgotPasswordForm(request.form)
	if form.validate_on_submit():
		# user = form.get_user()
		user = request.form['email']
		q = User.query.filter_by(email=user).first()
		# print(q.password)
		forgot_password(user, q.password)
		return redirect(request.args.get("next") or url_for("login"))	
	return render_template ("forgot_passwd.html", 
		title="Forgot Password", 
		form=form)

@app.route('/')
@app.route('/index')
@login_required
def index():
	user = g.user
	flash(user.lastSeen) 
	flash(str(date.today()))
	return render_template ("index.html",
		title = "Home", 
		user = user)
	# if user.lastSeen != str(date.today()):
	# 	return render_template ("index.html",
	# 		title = "Home", 
	# 		user = user)
	# else:
	# 	return render_template("comeback.html", title="Please come back later", user=user)

@app.route('/consent/')
def consent():
	return render_template('consent.html', title = "Consent")

@app.route('/logouthtml/')
def logouthtml():
	return render_template('logout.html', title="Logout")

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.before_request
def before_request():
	g.user = current_user

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.errorhandler(404)
def internal_error(error):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
	#uncommented next line, might cause instability
    db.session.rollback()
    return render_template('500.html'), 500

@app.after_request
def after_request(response):
	for query in get_debug_queries():
		if query.duration >= DATABASE_QUERY_TIMEOUT:
			app.logger.warning("SLOW QUERY: %s\nParameters: %s\nDuration: %fs\nContext: %s\n" % (query.statement, query.parameters, query.duration, query.context))
	return response

def flash_errors(form):
	for field, errors in form.errors.items():
		for error in errors:
			flash(u"Error in the %s field - %s" % (
			getattr(form, field).label.text,error
		))