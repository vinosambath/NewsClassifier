from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__);
app.config['MONGO_DBNAME'] = 'newsClassifierDB'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/newsClassifierDB'

mongo = PyMongo(app)
from newsClassifier import views