import unittest
from app.models import NewsArticles

class TestNewsArticle(unittest.TestCase):
    '''
    test the behaviour of the NewsArticles class
    '''
    def setUp(self):
        '''
        test that will run before every test
        '''
        self.new_NewsArticle = NewsArticles('Nation','http://corazon.com','Mary Paris', 'FRENCH KISSING','comment t\'allez vous', '2017-07-11T23:08:01Z', 'Nationmedia.co.ke')

    def test_init(self):
        '''
        test if object is instantiated correctly
        '''
        self.assertEqual(self.new_NewsArticle.source, "Nation")
        self.assertEqual(self.new_NewsArticle.urlToImage, "http://corazon.com")
        self.assertEqual(self.new_NewsArticle.author, "Mary Paris")
        self.assertEqual(self.new_NewsArticle.title, "FRENCH KISSING")
        self.assertEqual(self.new_NewsArticle.description, "comment t\'allez vous")
        self.assertEqual(self.new_NewsArticle.publishedAt, "2017-07-11T23:08:01Z")
        self.assertEqual(self.new_NewsArticle.ulr, "Nationmedia.co.ke")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_NewsArticle,NewsArticles))
