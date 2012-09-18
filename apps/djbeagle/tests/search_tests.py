from django.test import TestCase

from djbeagle.lib import search


class SearchTest(TestCase):
    def setUp(self):
        pass

    def test_get_engine_titles(self):
        engines = ["Google Scholar"]
        results = search.run(engines, "role based access control", 10)
        self.assertTrue(len(results) == 10)
    
