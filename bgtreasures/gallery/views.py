from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext

from django import http
from models import GalleryCategory, GalleryItem
from django.core import serializers
import simplejson as json

def gallery(request, gallery=None):
    cats = None

    if gallery in ['bridal', 'memorial', 'original']:
        v = "%s.html" % gallery
        if gallery in ['original']:
            cats = GalleryCategory.objects.all()
    else:
        raise Http404

    return render_to_response(v, {'cats': cats, 'gallery': gallery}, context_instance=RequestContext(request))

def gallery_item(request, gallery=None, id=None):
    item = get_object_or_404(GalleryItem, item_num=id)
    item_images = item.galleryitemimage_set.values('pk', 'image')
    item_images = json.dumps(list(item_images))
    return render_to_response('item.html', {'item': item, 'gallery': gallery, 'id': id, 'images': item_images}, context_instance=RequestContext(request))
