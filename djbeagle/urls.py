from django.conf.urls.defaults import *

urlpatterns = patterns('djbeagle.views',
    url(r'^$', 'home', name='home_url'),
)
