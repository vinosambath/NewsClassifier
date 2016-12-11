import urllib2
from BeautifulSoup 	import BeautifulSoup
from Exceptions import Exception

ex = Exception()
class scrapper:

	@ex.exceptionDeco
	def pageSoup(self, url):
		page = urllib2.urlopen(url)
		return BeautifulSoup(page.read())

#s = scrapper()
#print(s.pageSoup("http://timesofindia.indiatimes.com"))