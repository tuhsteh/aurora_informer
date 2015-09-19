from flask import Flask
import json
#import requests

app = Flask(__name__)
app.config.from_object('config')

from app import views


