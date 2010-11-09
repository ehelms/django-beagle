from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('djbeagle.views',
    url(r'^$', 'home', name='home_url'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', 
            { 'document_root' : settings.BASE_DIR + '/djbeagle/media/' }),
    )
