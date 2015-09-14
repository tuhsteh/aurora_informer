#!flask/bin/python
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class UnsubscribeForm(Form):
    openid = StringField('email', validators=[DataRequired()])