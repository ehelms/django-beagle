from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('djbeagle.views',
    url(r'^search/$', 'search', name='search_url'),
    url(r'^search/(?P<search_id>\d+)/$', 'search', name='search_url'),
    url(r'^search/(?P<search_id>\d+)/combined/$', 'combined_search', name='combined_search_url')
)
