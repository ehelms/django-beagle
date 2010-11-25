from django.test import TestCase

from djbeagle.lib.engines import util
from djbeagle.lib.engines.google_scholar import GoogleScholar

class UtilTest(TestCase):
    def test_get_engine_titles(self):
        titles = util.get_engine_titles()
        self.assertTrue("Google Scholar" in titles)
    
    def test_get_availible_engines(self):
        engines = util.get_availible_engines()
        self.assertTrue("Google Scholar" in engines)
        engine = engines["Google Scholar"]()
        self.assertTrue(isinstance(engine, GoogleScholar))

    def test_get_engine_class(self):
        klass = util.get_engine_class('djbeagle.lib.engines.google_scholar.GoogleScholar')
        self.assertTrue(isinstance(klass(), GoogleScholar))
