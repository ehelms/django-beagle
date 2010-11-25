import unittest

from djbeagle.tests import views_tests, engine_tests, search_tests

_testmodules = [views_tests, engine_tests, search_tests]

for module in _testmodules:
    for name,val in module.__dict__.iteritems():
        if name.endswith('Test'):
            globals()[name] = val

def suite():
    test_suite = unittest.TestSuite()
    for module in _testmodules:
        s = generate_testsuite(module.__dict__)
        test_suite.addTest(s)
    return test_suite

def generate_testsuite(globals):
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    for name,val in globals.iteritems():
        if name.endswith('Test'):
            test_suite.addTest(loader.loadTestsFromTestCase(val))
    return test_suite
