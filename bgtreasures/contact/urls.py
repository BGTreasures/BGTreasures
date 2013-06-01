from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('contact.views',
    url(r'^$', contact, name='contact'),
    url(r'^success/$', contact_success, name='contact_success'),
)
