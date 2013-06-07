from django.conf.urls import patterns, include, url
from django.contrib import admin

from gallery import urls
from contact import urls
from links import urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'bgtreasures.views.home', name='home'),
    url(r'^about$', 'bgtreasures.views.about', name='about'),
    url(r'^supplies$', 'bgtreasures.views.supplies', name='supplies'),
    url(r'^shows$', 'bgtreasures.views.shows', name='shows'),

    #apps
    url(r'^gallery/', include('gallery.urls')),
    url(r'^links/', include('links.urls')),
    url(r'^contact/', include('contact.urls')),

    #admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

#legacy urls
from django.views.generic.base import RedirectView
urlpatterns += patterns('',
    ('^[Ii]ndex.html?$', RedirectView.as_view(url='/', permanent=True)),
    ('^[Gg]allery.html?$', RedirectView.as_view(url='/gallery/original', permanent=True)),
    ('^pressed-flower-art$', RedirectView.as_view(url='/gallery/original', permanent=True)),
    ('^[Oo]ther_[Pp]roducts.html?$', RedirectView.as_view(url='/gallery/original', permanent=True)),
    ('^other-products$', RedirectView.as_view(url='/gallery/original', permanent=True)),
    ('^[Ss]hows.html?$', RedirectView.as_view(url='/shows', permanent=True)),
    ('^[Aa]bout.html?$', RedirectView.as_view(url='/about', permanent=True)),
    ('^[Cc]ontact.html?$', RedirectView.as_view(url='/contact/', permanent=True)),
)
