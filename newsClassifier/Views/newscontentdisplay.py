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

@login_required
def getNewsContentForThisUser():
	list = []
	news = News.objects[:5].order_by('added_time');
	return news