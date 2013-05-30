from django.conf.urls import patterns, include, url
from django.contrib import admin

from gallery import urls
from contact import urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'bgtreasures.views.home', name='home'),
    url(r'^about$', 'bgtreasures.views.about', name='about'),
    url(r'^supplies$', 'bgtreasures.views.supplies', name='supplies'),
    url(r'^shows$', 'bgtreasures.views.shows', name='shows'),
    url(r'^links$', 'bgtreasures.views.links', name='links'),

    #admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^gallery/', include('gallery.urls')),
)

urlpatterns += patterns('',
    url(r'^contact/', include('contact.urls')),
)

