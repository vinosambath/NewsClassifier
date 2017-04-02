from flask import Flask
from celery import Celery
from datetime import timedelta
from flask_mongoengine import MongoEngine
from flask.ext.login import LoginManager

app = Flask(__name__);
app.config['MONGODB_DB'] = 'newsClassifierDB'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/newsClassifierDB'
app.config['SECRET_KEY'] = 'H3@d#$XDA6'

login_manager = LoginManager()
login_manager.init_app(app)

def make_celery(app):
	celery = Celery(app.import_name, broker='redis://localhost:6379/0')
	return celery

celery = make_celery(app);
db = MongoEngine(app);

from newsClassifier.Views import loginsignup
from newsClassifier.Helpers import celeryTasks
