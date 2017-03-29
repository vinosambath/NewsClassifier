from newsClassifier import celery

import requests

@celery.task
def fetch_url(url):
	resp = requests.get(url)
	print resp.status_code
