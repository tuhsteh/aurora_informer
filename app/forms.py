#!flask/bin/python
#from flask.ext.wtf import Form
#from wtforms import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from flask_wtf import Form



class iSubscribe(Form):
    #user_email = StringField('email', validators=[DataRequired()]) # DataRequired ensures the form isn't empty.'
    user_name = StringField('user_name', validators=[DataRequired()]) # Not being used at the moment..