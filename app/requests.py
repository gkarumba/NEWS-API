import urllib.request,json
from .models import News

# Getting api key
api_key = None
# Getting the news & articles base url
news_base_url = None
news_articles_base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    news_articles_base_url = app.config['NEWS_ARTICLES_BASE_URL']