import urllib2
from urlparse import urljoin
import os
from BeautifulSoup 	import BeautifulSoup

class Scraper:

	def __init__(self):
		self.url = "http://timesofindia.indiatimes.com"

	def baseChecker(self, suburl, base):
		if suburl.startswith("http:"):
			return suburl
		return urljoin(base, suburl)

	def saveimage(self, title, sublink):

		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		'Accept-Encoding': 'none',
		'Accept-Language': 'en-US,en;q=0.8',
		'Connection': 'keep-alive'}

		req = urllib2.Request(sublink, headers=hdr)
		imagepage = urllib2.urlopen(req)
		imagesoup = BeautifulSoup(imagepage.read())

		texts1 = imagesoup.findAll("div", {"id" : "bellyad"})
		texts2= imagesoup.findAll("img", {"id" : "articleimg1"})
		#texts3 = imagesoup.find("div", {"class":"main-content"})
		texts4 = imagesoup.find("section", {"class":"highlight clearfix"})
		texts5 = imagesoup.find("div", {"class":"main-content"})
		imagelist = []
		initial = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bkpImages");
		path = initial
		if not os.path.exists(path):
			os.makedirs(path)

		filename = '%s/%s.jpg' % (path, title[:5].replace(" ",""))
		#imagelist.append(title[:5].replace(" ",""))
		retfilename = title[:5].replace(" ","")

		flag = 0

		for text in texts1:
			indexs = text.findAll('img')
			for index in indexs:
				try:
					urllib.urlretrieve(index['src'], filename)
				except:
					break
				flag = 1

		cnt = 0
		if flag == 0:
			try:
				for text in texts5:
					indexs = text.findAll('img')
					for index in indexs:
						#print baseChecker(index['src'], "http://timesofindia.indiatimes.com")
						try:
							urllib.urlretrieve(baseChecker(index['src'], "http://timesofindia.indiatimes.com"), filename)
							flag = 1
						except:
							break
						cnt = cnt + 1
						break
					if cnt == 1:
						break
			except:
				print "do nothing"



		if flag == 0 and texts2 is not None:
			for text in texts2:
				try:
					urllib.urlretrieve(text['src'], filename)
				except:
					break
				flag = 1

		if flag == 0 and texts4 is not None:
			for text in texts4:
				if text is not None:
					try:
						urllib.urlretrieve(baseChecker(text['src'], "http://timesofindia.indiatimes.com"), filename)
					except:
						break
				flag = 1


		# if flag == 0 and texts3 is not None:
		# 	for text in texts3:
		# 		indexs = text.findAll('img')
		# 		for index in indexs:
		# 			try:
		# 				urllib.urlretrieve(baseChecker(index['src'], "http://timesofindia.indiatimes.com"), filename)
		# 			except:
		# 				break
		# 			flag = 1
		# 			break

		return retfilename

	def scrapfromUrl(self, title, sublink):
		if sublink.startswith("http://www.cricbuzz.com"):
			return

		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		'Accept-Encoding': 'none',
		'Accept-Language': 'en-US,en;q=0.8',
		'Connection': 'keep-alive'}

		req = urllib2.Request(sublink, headers=hdr)
		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		'Accept-Encoding': 'none',
		'Accept-Language': 'en-US,en;q=0.8',
		'Connection': 'keep-alive'}

		req = urllib2.Request(sublink, headers=hdr)
		subpage = urllib2.urlopen(req)
		subsoup = BeautifulSoup(subpage.read())

		subtexts = subsoup.findAll("div", {"class" : "Normal"})
		textallsub = "print"
		for subtext in subtexts:
			textallsub = subtext.text

		subtexts = subsoup.findAll("div", {"class" : "content"})

		for subtext in subtexts:
				textallsub = subtext.text


		subtexts = subsoup.findAll("div", {"class" : "box12 one-third full-width clearfix no-image cmncssjsndiv"})

		for subtext in subtexts:
			textallsub = subtext.text


		return textallsub


	def base_newsContent_scaper(self):
		page = urllib2.urlopen(self.url)
		soup = BeautifulSoup(page.read())

		texts = soup.findAll("div", {"class" : "top-story"})

		newslinks = {}

		for text in texts:
			links = text.findAll('a')
			for link in links:
				newUrl = self.baseChecker(link['href'], self.url)
				if link.text:
					newslinks.update({newUrl:link.text})

		imagelist = []
		newsall = []
		newsTitle = []
		for newslink in newslinks:
			newsTitle.append(newslinks.get(newslink))
			imagelist.append(self.saveimage(newslinks.get(newslink), newslink))
			newsall.append(self.scrapfromUrl(newslinks.get(newslink), newslink))
		print zip(newsTitle, newsall, imagelist);
		return zip(newsTitle, newsall, imagelist)
