from flask import render_template
from flask.ext.mail import Message
from app import mail
from config import ADMINS

def user_notification(user):
    send_email("[Research Survey] %s is now a registered user, please follow the link to return to the Research Survey!" % user.email,
        ADMINS[0],
        [user.email],
        render_template("email/new_user_email.txt",
            user = user))

def forgot_password(user, password):
    send_email("[Research Survey] User %s Forgot Password" % user,
        ADMINS[0],
        [user],
        render_template("email/forgot_passwd.txt",
            user=user,
            password = password))

def send_email(subject, sender, recipients, text_body):
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = text_body
    mail.send(msg)