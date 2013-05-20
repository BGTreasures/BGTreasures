from django.conf.urls.defaults import *
from views import gallery, gallery_item

urlpatterns = patterns('gallery.views',
    url(r'^(?P<gallery>\w+)/$', gallery, name='gallery'),
    url(r'^(?P<gallery>\w+)/(?P<id>\d+)$', gallery_item, name='gallery_item'),
)
