import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_News = News(2,'Nation','Tech in the rise','Business','Nationmedia.co.ke')

    def test_init(self):
        '''
        test if object is instantiated correctly
        '''
        self.assertEqual(self.new_News.id, 1)
        self.assertEqual(self.new_News.description, 'Tech in the rise')
        self.assertEqual(self.new_News.name, 'Nation')
        self.assertEqual(self.new_News.url, 'Nationmedia.co.ke')
        self.assertEqual(self.new_News.category, 'Business')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_News,News))