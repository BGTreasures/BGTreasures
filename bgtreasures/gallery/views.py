from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from django import http
from models import GalleryCategory, GalleryItem

def gallery(request, gallery=None):
    v = ""
    cats = None
    if gallery in ['bridal', 'memorial', 'original', 'other']:
        v = "gallery_%s.html" % gallery

    if gallery in ['original']:
        cats = GalleryCategory.objects.all()

    return render_to_response(v, {'cats': cats, 'gallery': gallery}, context_instance=RequestContext(request))

def gallery_item(request, gallery=None, id=None):
	item = GalleryItem.objects.get(item_num=id)
	return render_to_response('item.html', {'item': item, 'gallery': gallery, 'id': id}, context_instance=RequestContext(request))