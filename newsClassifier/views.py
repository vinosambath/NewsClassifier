from newsClassifier import app
from newsClassifier import mongo
from newsClassifier import celeryTasks
import os


from newsScraper.scraper import Scraper

from flask import jsonify, send_from_directory

@app.route('/index')
def index():
	output = [];
	for s in mongo.db.news.find():
		output.append({"news": s['news']});
		#celeryTasks.fetch_url.delay("https://www.google.com")
		newsContentScraper= Scraper()
		output = newsContentScraper.base_newsContent_scaper()
	return jsonify({'result': output});

@app.route('/')
def main():
	path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates");
	print(path)
	return send_from_directory('/newsClassifier/templates', 'index.html');
