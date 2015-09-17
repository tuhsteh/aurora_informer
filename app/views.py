from flask import render_template, flash, redirect
from app import app
from .forms import iSubscribe


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    #if iSubscribe.validate_on_submit():
    #    print "someone clicked some shit"
    form = iSubscribe()
    if form.validate_on_submit:
        print  "somebody said %s" % str(form.user_name.data)# % user_email
    return render_template('index.html',
                           title='Aurora Informer', # <-- you can see how title gets populated in the ~/app/templates/base.html
                           form=form) 

@app.route('/unsubscribe')
def unsubscribe():
    return render_template('unsubscribe.html',
                           title='Unsubscribe from Aurora Informer')    