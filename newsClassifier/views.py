from newsClassifier import app
from newsClassifier import mongo
from flask import jsonify

@app.route('/')
@app.route('/index')
def index():
	output = [];
	for s in mongo.db.news.find():
		output.append({"news": s['news']});
	return jsonify({'result': output});