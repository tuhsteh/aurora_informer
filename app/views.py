from flask import render_template, flash, redirect
from app import app
from .forms import iSubscribe
from .forms import a_index
from .aurora_utils import get_geographic_latitude


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = a_index()
    return render_template('index.html',
                           title='Aurora Informer',
                           form=form)
    

@app.route('/subscribe', methods=['GET', 'POST'])
def registration():
    #if iSubscribe.validate_on_submit():
    #    print "someone clicked some shit"
    form = iSubscribe()
    if form.validate_on_submit():
        flash("did something!")
        usename = str(form.user_name.data)
        user_zip = str(form.user_zip.data)
        geographic_latitude = get_geographic_latitude(user_zip)
        print "User Name: %s" %usename
        print "User Email: %s" % str(form.user_email.data)
        print "User Zip Code: %s" % str(form.user_zip.data)
        print "Geographic Latitude: %s" % geographic_latitude
        
        return redirect('/')
    return render_template('subscribe.html',
                           title='Subscribe', # <-- you can see how title gets populated in the ~/app/templates/base.html
                           form=form) 
@app.route('/unsubscribe')
def unsubscribe():
    return render_template('unsubscribe.html',
                           title='Unsubscribe from Aurora Informer')    