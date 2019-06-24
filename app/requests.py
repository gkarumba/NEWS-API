import urllib.request,json
from .models import News,NewsArticles

# Getting api key
api_key = None
# Getting the news & articles base url
news_base_url = None
news_articles_base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    news_base_url = app.config['NEWS_API_BASE_URL']
    news_articles_base_url = app.config['NEWS_ARTICLES_BASE_URL']

def process_results(news_list):
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
            news_results = process_results(news_results_list)
            
    return new_results

def get_news_article(id):
    get_news_article_url = news_articles_base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_article_url) as url:
        news_article_data = url.read()
        news_article_response = json.loads(news_article_data)

        news_article = None
        if news_article_response:
            id = news_article_response.get('id')
            title = news_article_response.get('original_title')
            overview = news_article_response.get('overview')
            poster = news_article_response.get('poster_path')
            vote_average = news_article_response.get('vote_average')
            vote_count = news_article_response.get('vote_count')

            news_article = NewsArticles(id,title,overview,poster,vote_average,vote_count)

    return movie_object

def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None
        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)

    return search_movie_results

Movie = movie.Movie

