from pymongo import MongoClient

class db:

	_client = None
	def __init__(self):
		self._client = MongoClient()

	def getDbConnection(self, dbType):
		return self._client[dbType]

#db = db()
#db.getDbConnection("newscontentdb")