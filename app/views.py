from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title="home", amount="3000")

@app.route('/')
@app.route('/impact')
def impact():
	return render_template('impact.html', title="impact")

@app.route('/')
@app.route('/news')
def news():
	return render_template('news.html', title="news")

@app.route('/')
@app.route('/give')
def give():
	return render_template('give.html', title='give')