import datetime

from mongoengine import *
from mongoengine import Document
from newsClassifier import db

class News(Document):
    news_id = SequenceField(required=True, primary_key=True)
    news_title = db.StringField()
    news_content = db.StringField()
    added_time = DateTimeField(default=datetime.datetime.now)
    meta = {'strict': False}