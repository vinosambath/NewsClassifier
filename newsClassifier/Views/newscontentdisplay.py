from newsClassifier import app
from flask import jsonify, send_from_directory, request, render_template, flash, Response
from flask.ext.login import login_required, login_user, logout_user, current_user
from newsClassifier import login_manager
from newsClassifier.Helpers import LoginFlask
from newsClassifier.Models.news import News


@app.route('/newscontent')
@login_required
def newscontent():
	news = getNewsContentForThisUser();
	return render_template('newscontentdisplay.html', news=news)

@app.route('/newsfetcher')
@login_required
def newsfetcher():
	start = request.args.get('start');
	end = request.args.get('end')
	news = getNewsContentForThisUser(start, end);
	return news.to_json()

@login_required
def getNewsContentForThisUser(start = 0, end = 5):
	list = []
	news = News.objects[int(start):int(end)].order_by('added_time');
	return news