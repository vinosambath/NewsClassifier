from newsClassifier import celery
from celery.decorators import periodic_task
from datetime import timedelta
from newsScraper.scraper import Scraper
from newsClassifier.Models.news import News

import requests

scraperObj = Scraper();

@celery.task
def fetch_url():
	value = scraperObj.base_newsContent_scaper();
	for key in value:
		news = News();
		if not News.objects(news_title = key[0]):
			news.news_title = key[0]
			news.news_content = key[1]
			try:
				news.save()
			except:
				print("Error occured")
		else:
			print("Skipped as they already exist")

@periodic_task(run_every=timedelta(seconds=40))
def hello():
	fetch_url()
