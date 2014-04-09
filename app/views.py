from flask import abort, render_template, Response, flash, redirect, session, url_for, g, request, send_from_directory
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from forms import LoginForm, RegistrationForm
from models import User, ROLE_USER, ROLE_ADMIN

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

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
	user = g.user
	return render_template ("forgot_passwd.html", title="Forgot Password")

@app.route('/')
@app.route('/index')
# @login_required
def index():
	user = g.user
	return render_template ("index.html",
		title = "Home", 
		user = user)

@app.route('/about')
def about():
	return render_template("about.html",
		title = "About")

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

