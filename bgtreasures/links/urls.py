from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('links.views',
    url(r'^$', contact, name='links'),
)
