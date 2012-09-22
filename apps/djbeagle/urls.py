from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('djbeagle.views',
    url(r'^$', 'home', name='home_url'),
    url(r'^search/$', 'search', name='search_url'),
)
