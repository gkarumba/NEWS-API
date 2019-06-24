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
        return redirect(url_for('search',news_name = news_name))
    else:
        return render_template('index.html',message = message, title = title)