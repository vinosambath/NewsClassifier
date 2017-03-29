from newsClassifier import app
from newsClassifier import mongo
from newsClassifier import celeryTasks


from newsScraper.scraper import Scraper

from flask import jsonify

@app.route('/')
@app.route('/index')
def index():
	output = [];
	for s in mongo.db.news.find():
		output.append({"news": s['news']});
		celeryTasks.fetch_url.delay("https://www.google.com")
		newsContentScraper= Scraper()
		newsContentScraper.base_newsContent_scaper()
	return jsonify({'result': output});