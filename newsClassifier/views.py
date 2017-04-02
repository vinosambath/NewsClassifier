from newsClassifier import app
from newsClassifier import celeryTasks
from Models.user import User
import os

from newsScraper.scraper import Scraper
from flask import jsonify, send_from_directory, request, render_template, flash, Response
from flask.ext.login import login_required, login_user, logout_user, current_user
from newsClassifier import login_manager
from newsClassifier.Helpers import LoginFlask

@app.route('/index')
@app.route('/')
@login_required
def index():
	if current_user.is_authenticated:
		print("HELLO")
		return logout()
	else:
		print "no";
		return login()

@app.route('/logout')
def logout():
	logout_user();
	return Response('<p>Logged Out</p>')

@app.route('/register' , methods=['GET','POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	email = request.form['email']
	password = request.form['password']
	user = User();
	user.password = password
	user.email = email
	print(user)
	try:
		user.save()
	except:
		print('Failed')
		flash('Registration Failed. Email may be already with us!')
		return render_template('register.html')
	else:
		login_user(user)
		return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	email = request.form['email']
	password = request.form['password']
	user = User.objects(email = email)
	if user[0].password == password:
		print("logged")
		login_user(user[0])
	else:
		print("not logged")

	return render_template('login.html')
