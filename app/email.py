from app import mail
from flask.ext.mail import Message
from decorators import async
from flask import render_template
from config import ADMINS

def user_notification(user):
    send_email("[Research Survey] %s is now a registered user, please follow the link to return to the Research Survey!" % user.email,
        ADMINS[0],
        [user.email],
        render_template("new_user_email.txt", 
            user = user))

def forgot_password(user):
    send_email("[Research Survey] User %s Forgot Password" % user.email,
        ADMINS[0],
        [user.email],
        render_template("forgot_passwd.txt", 
            user=user))

@async
def send_async_email(msg):
    mail.send(msg)

def send_email(subject, sender, recipients, text_body):
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = text_body
    send_async_email(msg)