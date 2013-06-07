from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('links.views',
    url(r'^$', links, name='links'),
)
