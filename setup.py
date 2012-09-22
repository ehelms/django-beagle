#!/usr/bin/env python

from setuptools import setup

setup(
    name='django-beagle',
    version='1.0',
    description='',
    author='Eric D. Helms',
    author_email='ericdhelms@gmail.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=['Django>=1.4', 'gdata', 'BeautifulSoup', 'python-openid', 'south', 'psycopg2'],
)
