from flask import Flask
from celery import Celery
from flask_pymongo import PyMongo

app = Flask(__name__);
app.config['MONGO_DBNAME'] = 'newsClassifierDB'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/newsClassifierDB'

def make_celery(app):
	celery = Celery(app.import_name, broker='redis://localhost:6379/0')
	# TaskBase = celery.Task
	# class ContextTask(TaskBase):
	# 	abstract = True
	# 	def __call__(self, *args, **kwargs):
	# 		with app.app_context():
	# 			return TaskBase.__call__(self, *args, **kwargs)

	# celery.Task = ContextTask
	return celery

celery = make_celery(app);

print(celery)

mongo = PyMongo(app)
from newsClassifier import views