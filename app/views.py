#FLASK
from flask import abort, render_template, Response, flash, redirect, session
from flask import url_for, g, request, send_from_directory
#FLASK EXTENSIONS
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext.sqlalchemy import get_debug_queries
from flask.ext.mail import Mail
#LOCAL
from models import User, ROLE_USER, ROLE_ADMIN, Survey1, Survey2, Survey3, Survey4
from forms import LoginForm, RegistrationForm, Survey1Form, Survey2Form, Survey3Form
from forms import Survey4Form, NewPass, ForgotPasswordForm
from email import user_notification, forgot_password
from config import DATABASE_QUERY_TIMEOUT
from app import app, db, lm, mail, models
from decorators import admin_required
#OTHER
from  datetime import date, timedelta
import uuid


@app.route('/survey_1/', methods=['GET','POST'])
@login_required
def survey_1():
	g.user = current_user
	if g.user.s1 is False:
		form = Survey1Form(request.form)

		if form.validate_on_submit():
			survey = Survey1()
			form.populate_obj(survey)
			survey.user = g.user
			db.session.add(survey)

			g.user.s1 = True
			g.user.lastSeen = date.today()
			db.session.commit()
			logout_user()
			return redirect(url_for('logouthtml'))

		return render_template('survey/Survey1.html', title='Survey', form=form)
	else:
		return redirect(url_for('index'))

@app.route('/survey_2/', methods=['GET','POST'])
@login_required
def survey_2():
	g.user = current_user
	if g.user.s1 is not False and g.user.s2 is False:
		form = Survey2Form(request.form)

		if form.validate_on_submit():
			survey = Survey2()
			form.populate_obj(survey)
			survey.user = g.user
			db.session.add(survey)

			g.user.s2 = True
			g.user.lastSeen = date.today()
			db.session.commit()
			logout_user()
			return redirect(url_for('logouthtml'))

		return render_template('survey/Survey2.html', title='Survey', form=form)
	else:
		return redirect(url_for('index'))


@app.route('/survey_3/', methods=['GET','POST'])
@login_required
def survey_3():
	g.user = current_user
	if g.user.s2 is not False and g.user.s3 is False:

		if g.user.changedPass is False:
			return redirect(url_for('new_pass'))

		form = Survey3Form(request.form)

		if form.validate_on_submit():
			survey = Survey3()
			form.populate_obj(survey)
			survey.user = g.user
			db.session.add(survey)

			g.user.s3 = True
			g.user.lastSeen = date.today()
			db.session.commit()
			logout_user()
			return redirect(url_for('logouthtml'))

		return render_template('survey/Survey3.html', title='Survey', form=form)
	else:
		return redirect(url_for('index'))


@app.route('/survey_4/', methods=['GET','POST'])
@login_required
def survey_4():
	g.user = current_user
	if g.user.s3 is not False and g.user.s4 is False:

		if g.user.changedPass is False:
			return redirect(url_for('new_pass'))

		form = Survey4Form(request.form)

		if form.validate_on_submit():

			survey = Survey4()
			form.populate_obj(survey)
			survey.user = g.user
			db.session.add(survey)

			g.user.s4 = True
			g.user.lastSeen = date.today()
			db.session.commit()
			logout_user()
			return render_template("final.html", title="Thanks!")

		return render_template('survey/Survey4.html', title='Survey', form=form)
	else:
		return redirect(url_for('index'))


@app.route('/create_acct/' , methods=['GET','POST'])
def create_acct():
	form = RegistrationForm(request.form)
	if form.validate_on_submit():
		user = User(email=form.email.data, password=form.password.data,
			oldPassword=form.password.data, userid=(str(uuid.uuid1())))
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
		user = g.user
		print form.data
		if user.password == form.data['password']:
				print 'I should raise a validation error'
				form.password.errors.append('You\'ve already used this password. Please choose a new password.')
		else:
				print 'user picked a different password'
				user.password = form.password.data
				user.changedPass = True
				db.session.commit()
				return redirect(url_for('index'))

	return render_template('new_pass.html', title='Update Password', form=form)

@app.route('/login/',methods=['GET','POST'])
def login():
	form = LoginForm(request.form)
	if form.validate_on_submit():
		user = form.get_user()
		login_user(user)
		user = g.user
		if current_user.is_admin():
			return redirect(url_for('admin'))
		elif user.s2 is True and user.s3 is False:
			return redirect(request.args.get("next") or url_for("new_pass"))
		else:
			return redirect(request.args.get("next") or url_for("index"))
	return render_template('login.html', title="Login", form=form)

@app.route('/forgot_passwd', methods=['GET', 'POST'])
def forgot_passwd():
	form = ForgotPasswordForm(request.form)
	if form.validate_on_submit():
		user = request.form['email']
		if User.query.filter_by(email=user).first():
			q = User.query.filter_by(email=user).first()
			forgot_password(user, q.password)
			return redirect(request.args.get("next") or url_for("login"))
		else:
			flash('Username not found')
			return redirect(request.args.get("next") or url_for("login"))
	return render_template ("forgot_passwd.html",
		title="Forgot Password",
		form=form)

@app.route('/')
@app.route('/index')
@login_required
def index():
	user = g.user
	if user.is_admin():
		return redirect(url_for('admin'))
	return render_template ("index.html", title="Home", user=user)
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


@app.route('/admin')
@login_required
@admin_required
def admin():
	users = User.query.filter_by(role=0)
	return render_template('admin/index.html', title="Admin", users=users)

@app.route('/admin_survey1/')
@login_required
@admin_required
def admin_survey1():
	surveys = Survey1.query.all()
	return render_template('admin/partials/survey1.html', title='Admin Survey-1', surveys=surveys)

@app.route('/admin_survey2/')
@login_required
@admin_required
def admin_survey2():
	surveys = Survey2.query.all()
	return render_template('admin/partials/survey2.html', title='Admin Survey-2', surveys=surveys)

@app.route('/admin_survey3/')
@login_required
@admin_required
def admin_survey3():
	surveys = Survey3.query.all()
	return render_template('admin/partials/survey3.html', title='Admin Survey-3', surveys=surveys)

@app.route('/admin_survey4/')
@login_required
@admin_required
def admin_survey4():
	surveys = Survey4.query.all()
	return render_template('admin/partials/survey4.html', title='Admin Survey-4', surveys=surveys)

