from flask import render_template,request,redirect,url_for
from . import main
from ..models import News,NewsArticles
from ..requests import get_news,get_news_article,search_news,get_all_news

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Hello World'
    message = 'Home - Welcome to The best Online News Source'
    search_news = request.args.get('news_name')
    if search_news:
        return redirect(url_for('search.html',news_name = search_news))
    else:
        return render_template('index.html',message = message, title = title)

@main.route('/sports')
def sport():
	'''
	View root page function that returns the sports page and its data
	'''

	sports = get_news_article('sports')
	return render_template('sports.html',news_articles=sports)

@main.route('/business')
def business():
	'''
	View root page function that returns the business page and its data
	'''

	business = get_news_article('business')
	return render_template('business.html',news_articles=business)

@main.route('/entertainment')
def entertainment():
	'''
	View root page function that returns the entertainment page and its data
	'''s
	entertainment = get_news_article('entertainment')
	return render_template('entertainment.html',news_articles=entertainment)