import urllib2
from BeautifulSoup 	import BeautifulSoup


class scrapper:

	def pageSoup(self, url):
		try:
			page = urllib2.urlopen(url)
			return BeautifulSoup(page.read())
		except:
			print("Unexpected error")

#s = scrapper()
#print(s.pageSoup("http://timesofindia.indiatimes.com"))