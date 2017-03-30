from newsClassifier import celery
from newsScraper.scraper import Scraper

import requests

scraperObj = Scraper();

@celery.task
def fetch_url(url):
	resp = requests.get(url)
	print(scraperObj.base_newsContent_scaper());
	print resp.status_code
