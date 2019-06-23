class News:
    '''
    News class to define News Objects
    '''

    def __init__(self):
        self.id =id
        


class NewsArticles:

    all_NewsArticles = []

    def __init__(self):
        


    def save_newsArticle(self):
        NewsArticles.all_NewsArticles.append(self)


    @classmethod
    def clear_newsArticles(cls):
        NewsArticles.all_NewsArticles.clear()

    @classmethod
    def get_newsArticles(cls,id):

        response = []

        for newsArticle in cls.all_NewsArticles:
            if newsArticle.movie_id == id:
                response.append(newsArticle)

        return response