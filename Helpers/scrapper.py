import urllib2
from BeautifulSoup 	import BeautifulSoup


class scrapper:

	def pageSoup(self, url):	
		page = urllib2.urlopen(url)
		return BeautifulSoup(page.read())

#s = scrapper()
#print(s.pageSoup("http://timesofindia.indiatimes.com"))