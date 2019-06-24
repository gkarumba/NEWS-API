import urllib.request,json
from .models import News,NewsArticles

# Getting api key
api_key = None
# Getting the news & articles base url
news_base_url = None
news_articles_base_url = None

def configure_request(app):
    global api_key,news_base_url,news_articles_base_url
    api_key = app.config['NEWS_API_KEY']
    news_base_url = app.config['NEWS_API_BASE_URL']
    news_articles_base_url = app.config['NEWS_ARTICLES_API_BASE_URL']

def news_process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        category = news_item.get('category')
        url = news_item.get('url')
        if name:
            news_object = News(id,name,description,category, url)
            news_results.append(news_object)
            
    return news_results

def article_process_results(news_article_list):
    '''
    Function  that processes the news article result and transform them to a list of Objects

    Args:
        news_article_list: A list of dictionaries that contain news details

    Returns :
        news_article_results: A list of news objects
    '''
    news_article_results = []
    for news_article_item in news_article_list:
        source = news_article_item.get('source')
        urlToImage = news_article_item.get('urlToImage')
        title = news_article_item.get('title')
        description = news_article_item.get('description')
        publishedAt = news_article_item.get('publishedAt')
        url = news_article_item.get('url')

        if title:
            news_article_object = NewsArticles(id,source, urlToImage, author,title,description,publishedAt,url)
            news_article_results.append(news_article_object)
            
    return news_article_results

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None
        
        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = news_process_results(news_results_list)
            
    return new_results

def get_news_article(id):
    get_news_article_url = news_articles_base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_article_url) as url:
        news_article_data = url.read()
        news_article_response = json.loads(news_article_data)

        news_article = None
        if news_article_response['articles']:
            news_article_result_list = news_article_data['articles']
            news_article_results = article_process_results(news_article_result_list)
    return news_article_results

def search_news(news_name):
    search_news_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(news_name,api_key)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None
        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_news_results = article_process_results(search_news_list)

    return search_news_results

def get_all_news(source):
    source_news_url = 'https://newsapi.org/v2/everything?domains={}&language=en&apiKey={}'.format(source, api_key)

    with urllib.request.urlopen(source_news_url) as url:
        source_news_data = url.read()
        source_news_response = json.loads(source_news_data)

        source_news_results = None

        if source_news_response['articles']:
            source_news_list = source_news_response['articles']
            source_news_results = process_article_results(source_news_list)
    
    return source_news_results


