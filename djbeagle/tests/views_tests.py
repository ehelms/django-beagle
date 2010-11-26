from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from djbeagle.models import Search, Article


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create(username='TestUser1')
        self.client.login(username=self.user1.username)
    
    def test_search_post(self):
        response = self.client.post('/djbeagle/search/',
                        { 'engine' : 'Google Scholar', 
                         'criteria' : 'role based access control' })
        self.assertEquals(response.status_code, 200)
        self.assertNotContains(response, "fail")
    
    def test_search_post_articles_created(self):
        response = self.client.post('/djbeagle/search/',
                        { 'engine' : 'Google Scholar', 
                         'criteria' : 'role based access control' })
        self.assertEquals(response.status_code, 200)
        articles = Article.objects.all()
        self.assertTrue(len(articles) == 10)
