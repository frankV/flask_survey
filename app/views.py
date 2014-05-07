#FLASK
from flask import abort, render_template, Response, flash, redirect, session, url_for, g, request, send_from_directory
#FLASK EXTENSIONS
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext.sqlalchemy import get_debug_queries
from flask.ext.mail import Mail
#LOCAL
from models import User, ROLE_USER, ROLE_ADMIN
from forms import LoginForm, RegistrationForm, Survey1, Survey2, Survey3, Survey4
from email import user_notification
from config import DATABASE_QUERY_TIMEOUT
from app import app, db, lm, mail

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.route('/survey_1/', methods=['GET','POST'])
@login_required
def survey_1():
	form = Survey1(request.form)
	if form.validate_on_submit():
		print form
		# form.populate_obj(survey3)
		db.session.add(form)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('Survey1.html', title='Survey', form=form)

@app.route('/survey_2/', methods=['GET','POST'])
@login_required
def survey_2():
	form = Survey2(request.form)
	if form.validate_on_submit():
		print form
		# form.populate_obj(survey3)
		db.session.add(form)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('Survey2.html', title='Survey', form=form)

@app.route('/survey_3/', methods=['GET','POST'])
@login_required
def survey_3():
	form = Survey3(request.form)
	if form.validate_on_submit():
		print form
		# form.populate_obj(survey3)
		db.session.add(form)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('Survey3.html', title='Survey', form=form)

@app.route('/survey_4/', methods=['GET','POST'])
@login_required
def survey_4():
	form = Survey4(request.form)
	if form.validate_on_submit():
		print form
		# form.populate_obj(survey3)
		db.session.add(form)
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
		user_notification(user
			)
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
	form = ForgotPassword(request.form)
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