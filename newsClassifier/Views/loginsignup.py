from newsClassifier import app
from newsClassifier import celeryTasks
from newsClassifier.Models.user import User
from newsClassifier.Views import newscontentdisplay
import os

from newsScraper.scraper import Scraper
from flask import jsonify, send_from_directory, request, render_template, flash, Response, redirect
from flask.ext.login import login_required, login_user, logout_user, current_user
from newsClassifier import login_manager
from newsClassifier.Helpers import LoginFlask

@app.route('/index')
@app.route('/')
def index():
	if current_user.is_authenticated:
		return redirect('/newscontent')
	else:
		return redirect('/login')

@app.route('/logout')
@login_required
def logout():
	print(current_user)
	logout_user();
	message = "Successfully logged out!"
	flash(message)
	return redirect('/login')

@app.route('/register' , methods=['GET','POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	email = request.form['email']
	password = request.form['password']
	user = User();
	user.password = password
	user.email = email
	try:
		user.save()
	except:
		print('Failed')
		flash('Registration Failed. Email may be already with us!')
		return redirect('/register')
	else:
		login_user(user)
		return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect('/newscontent')
	if request.method == 'GET':
		return render_template('login.html')
	email = request.form['email']
	password = request.form['password']
	user = User.objects(email = email)
	if user[0].password == password:
		login_user(user[0])
		return redirect('/')
	else:
		return redirect('/register')
