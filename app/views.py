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
from app import app, db, lm, mail, fail_log
#OTHER
from  datetime import date, timedelta
import uuid

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.route('/survey_1/', methods=['GET','POST'])
@login_required
def survey_1():
	g.user = current_user
	if g.user.s1 is False:
		form = Survey1Form(request.form)
		if form.validate_on_submit():
			g.user.s1=True
			g.user.lastSeen=date.today()
			model = Survey1(gender=form.gender.data, age=form.age.data, 
				education=form.education.data, language=form.language.data, userid=g.user.userid)

			form.populate_obj(model)
			db.session.add(model)		
			db.session.add(g.user)
			db.session.commit()
			# logout_user()
			return redirect(url_for('logouthtml'))
		return render_template('Survey1.html', title='Survey', form=form)
	else:
		return redirect(url_for('index'))

@app.route('/survey_2/', methods=['GET','POST'])
@login_required
def survey_2():
	g.user = current_user
	if g.user.s1 is not False and g.user.s2 is False:
		form = Survey2Form(request.form)
		if form.validate_on_submit():	
			g.user.s2=True
			g.user.lastSeen=date.today()
			model=Survey2(major=form.major.data, department=form.department.data, 
				count=form.count.data, unique=form.unique.data, userid=g.user.userid)
			
			form.populate_obj(model)
			db.session.add(model)		
			db.session.add(g.user)
			db.session.commit()
			# logout_user()
			return redirect(url_for('logouthtml'))
		return render_template('Survey2.html', title='Survey', form=form)
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
			g.user.s3=True
			g.user.lastSeen=date.today()
			model = Survey3(choose_names=form.choose_names.data, choose_numbers=form.choose_numbers.data, 
				choose_songs=form.choose_songs.data, choose_mnemonic=form.choose_mnemonic.data, 
				choose_sports=form.choose_sports.data, choose_famous=form.choose_famous.data, 
				choose_words=form.choose_words.data, choose_O=form.choose_O.data, secure_numbers=form.secure_numbers.data, 
				secure_upper_case=form.secure_upper_case.data, secure_symbols=form.secure_symbols.data, 
				secure_eight_chars=form.secure_eight_chars.data, secure_no_dict=form.secure_no_dict.data, 
				secure_adjacent=form.secure_adjacent.data, secure_nothing=form.secure_nothing.data, secure_O=form.secure_O.data,
				modify=form.modify.data, word_part_N=form.word_part_N.data, word_part_changed_completely=form.word_part_changed_completely.data,
				word_part_changed_slightly=form.word_part_changed_slightly.data, word_part_capitalized_letters=form.word_part_capitalized_letters .data, 
				word_part_O=form.word_part_O, usedPassword=form.usedPassword.data,
				number_N=form.number_N.data, number_added_digits=form.number_added_digits.data, 
				number_deleted_digits=form.number_deleted_digits.data, 
				number_substituted_digits=form.number_substituted_digits.data,number_O=form.number_O.data,
				char_N = form.char_N.data, char_added_symbols=form.char_added_symbols.data,
				char_deleted_symbols=form.char_deleted_symbols.data, char_substituted_symbols=form.char_substituted_symbols.data,
				char_O=form.char_O.data, userid=g.user.userid)
			
			form.populate_obj(model)
			db.session.add(g.user)
			db.session.add(model)
			db.session.commit()
			# logout_user()
			return redirect(url_for('logouthtml'))
		return render_template('Survey3.html', title='Survey', form=form)
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
			g.user.s4=True
			g.user.lastSeen=date.today()
			model = Survey4(computerTime=form.computerTime.data, comments=form.comments.data, 
				pass_random=form.pass_random.data, pass_reuse=form.pass_reuse.data, 
				pass_modify=form.pass_modify.data, pass_new=form.pass_new.data, 
				pass_substitute=form.pass_substitute.data, pass_multiword=form.pass_multiword.data,
				pass_phrase=form.pass_phrase.data, pass_O=form.pass_O.data, 
				how_regular_file=form.how_regular_file.data, how_encrypted=form.how_encrypted.data,
				how_software=form.how_software.data, how_cellphone=form.how_cellphone.data,
				how_browser=form.how_browser.data, how_write_down=form.how_write_down.data, 
				how_no=form.how_no.data, userid=g.user.userid)
			
			form.populate_obj(model)
			db.session.add(g.user)
			db.session.add(model)
			db.session.commit()
			# logout_user()
			return render_template("final.html", title="Thanks!")
		return render_template('Survey4.html', title='Survey', form=form)
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
		user.password = form.password.data
		user.changedPass=True
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template('new_pass.html', title='Update Password', form=form)

@app.route('/login/',methods=['GET','POST'])
def login():
	form = LoginForm(request.form)
	if form.validate_on_submit():
		user = form.get_user()
		login_user(user)
		session.permanent = True
		app.permanent_session_lifetime = timedelta(minutes=25)
		user = g.user
		if user.s2 is True and user.s3 is False:
			return redirect(request.args.get("next") or url_for("new_pass"))
		else:
			return redirect(request.args.get("next") or url_for("index"))
	return render_template('login.html', title = "Login", form=form)

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
