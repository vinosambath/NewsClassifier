import yaml

class configParser:

	_cfg = None
	def __init__(self):
		try:
			with open("../config.yaml", 'r') as ymlfile:
				self._cfg = yaml.load(ymlfile)
		except:
			print("Exception occured")

	def getDbName(self):
		return self._cfg['db']['dbname']

cp = configParser()
print(cp.getDbName())