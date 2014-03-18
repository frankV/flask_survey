from decorators import async
from flask import render_template
from config import ADMINS

def user_notification(user):
    send_email("[Research Survey] %s is now a registered user, please follow the link to return to the Research Survey!" % user.username,
        ADMINS[0],
        [user.username],
        render_template("new_user_email.txt", 
            user = user))

@async
def send_async_email(msg):
    mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(msg)