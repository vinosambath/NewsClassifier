import datetime

from mongoengine import *
from mongoengine import Document
from newsClassifier import db

class User(Document):
	email = db.StringField(required=True, unique=True)
	password = db.StringField()
	join_date = DateTimeField(default=datetime.datetime.now)
	meta = {'strict': False}

	def __unicode__(self):
		return '%s %s' %(self.email, self.password)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)
