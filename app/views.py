#FLASK
from flask import abort, render_template, Response, flash, redirect, session, url_for, g, request, send_from_directory
#FLASK EXTENSIONS
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext.sqlalchemy import get_debug_queries
from flask.ext.mail import Mail
#LOCAL
from models import User, ROLE_USER, ROLE_ADMIN, Survey1, Survey2, Survey3, Survey4
from forms import LoginForm, RegistrationForm, Survey1Form, Survey2Form, Survey3Form, Survey4Form
from email import user_notification
from config import DATABASE_QUERY_TIMEOUT
from app import app, db, lm, mail
#OTHER
from datetime import datetime

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.route('/survey_1/', methods=['GET','POST'])
@login_required
def survey_1():
	g.user = current_user
	form = Survey1Form(request.form)
	if form.validate_on_submit():
		model = Survey1(gender=form.gender.data, age=form.age.data, education=form.education.data, language=form.language.data)
		form.populate_obj(model)
		db.session.add(model)
		db.session.commit()
		g.user.s1=True
		g.user.lastSeen=datetime.utcnow()
		db.session.add(g.user)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('Survey1.html', title='Survey', form=form)

@app.route('/survey_2/', methods=['GET','POST'])
@login_required
def survey_2():
	g.user = current_user
	form = Survey2Form(request.form)
	if form.validate_on_submit():
		model=Survey2(major=form.major.data, department=form.department.data, count=form.count.data, unique=form.unique.data)
		form.populate_obj(model)
		db.session.add(model)
		db.session.commit()
		g.user.s2=True
		g.user.lastSeen=datetime.utcnow()
		db.session.add(g.user)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('Survey2.html', title='Survey', form=form)

@app.route('/survey_3/', methods=['GET','POST'])
@login_required
def survey_3():
	g.user = current_user
	form = Survey3Form(request.form)
	if form.validate_on_submit():
		model = Survey3(choose=form.choose.data, secure=form.secure.data, modify=form.modify.data, usedPassword=form.usedPassword.data, wordPart=form.wordPart.data, numberPart=form.numberPart.data, charPart=form.charPart.data)
		form.populate_obj(model)
		db.session.add(model)
		db.session.commit()
		g.user.s3=True
		g.user.lastSeen=datetime.utcnow()
		db.session.add(g.user)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('Survey3.html', title='Survey', form=form)

@app.route('/survey_4/', methods=['GET','POST'])
@login_required
def survey_4():
	g.user = current_user
	form = Survey4Form(request.form)
	if form.validate_on_submit():
		model = Survey4(computerTime=forms.computerTime.data, passwordCreation=forms.passwordCreation.data, storePasswords=form.storePasswords.data, howStored=forms.howStored.data, comments=form.comments.data)
		form.populate_obj(model)
		db.session.add(model)
		db.session.commit()
		g.user.s4=True
		g.user.lastSeen=datetime.utcnow()
		db.session.add(g.user)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('Survey4.html', title='Survey', form=form)

@app.route('/create_acct/' , methods=['GET','POST'])
def create_acct():
	form = RegistrationForm(request.form)
	if form.validate_on_submit():
		print form
		user = User()
		form.populate_obj(user)
		db.session.add(user)
		db.session.commit()
		login_user(user)
		user_notification(user)
		return redirect(url_for('index'))
	return render_template('create_acct.html', title = "Create Account", form=form)

@app.route('/login/',methods=['GET','POST'])
def login():
	form = LoginForm(request.form)
	if form.validate_on_submit():
		user = form.get_user()
		login_user(user)
		flash("Logged in successfully.")
		return redirect(request.args.get("next") or url_for("index"))
	return render_template('login.html', title = "Login", form=form)

@app.route('/forgot_passwd')
def forgot_passwd():
	form = ForgotPasswordForm(request.form)
	if form.validate_on_submit():
		user = form.get_user()

	return render_template ("forgot_passwd.html", title="Forgot Password")

@app.route('/')
@app.route('/index')
@login_required
def index():
	user = g.user
	return render_template ("index.html",
		title = "Home", 
		user = user)

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.before_request
def before_request():
	g.user = current_user

@app.route('/logout')
def logout():
	#double check if the 
	logout_user()
	return redirect(url_for('index'))

@app.errorhandler(404)
def internal_error(error):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    # db.session.rollback()
    return render_template('500.html'), 500

@app.after_request
def after_request(response):
	for query in get_debug_queries():
		if query.duration >= DATABASE_QUERY_TIMEOUT:
			app.logger.warning("SLOW QUERY: %s\nParameters: %s\nDuration: %fs\nContext: %s\n" % (query.statement, query.parameters, query.duration, query.context))
	return response