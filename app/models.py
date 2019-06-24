class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,name,description,category, url):
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.url = url
		


class NewsArticles:

    all_NewsArticles = []

    def __init__(self,source, urlToImage, author,title,description,publishedAt,url):
        self.source = source
        self.urlToImage = urlToImage
        self.author = author
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.url = url


    def save_newsArticle(self):
        NewsArticles.all_NewsArticles.append(self)


    @classmethod
    def clear_newsArticles(cls):
        NewsArticles.all_NewsArticles.clear()

    @classmethod
    def get_newsArticles(cls,id):

        response = []

        for newsArticle in cls.all_NewsArticles:
            if newsArticle.id == id:
                response.append(newsArticle)

        return response