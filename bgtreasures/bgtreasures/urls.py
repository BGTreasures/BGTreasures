from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'bgtreasures.views.home', name='home'),
    url(r'^about$', 'bgtreasures.views.about', name='about'),
    url(r'^supplies$', 'bgtreasures.views.supplies', name='supplies'),
    url(r'^shows$', 'bgtreasures.views.shows', name='shows'),
    url(r'^links$', 'bgtreasures.views.links', name='links'),
    url(r'^contact/$', 'bgtreasures.views.contact', name='contact'),
    url(r'^contact_success$', 'bgtreasures.views.contact_success', name='contact_success'),

    #TODO: put these in gallery app
    url(r'^gallery/(?P<gallery>\w+)/$', 'gallery.views.gallery', name='gallery'),
    url(r'^gallery/(?P<gallery>\w+)/(?P<id>\d+)$', 'gallery.views.gallery_item', name='gallery_item'),
    
    # Examples:
    # url(r'^$', 'bgtreasures.views.home', name='home'),
    # url(r'^bgtreasures/', include('bgtreasures.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
