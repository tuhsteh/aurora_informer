from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Aurora Informer Home')

@app.route('/unsubscribe')
def unsubscribe():
    return render_template('unsubscribe.html',
                           title='Unsubscribe Aurora Informer')    