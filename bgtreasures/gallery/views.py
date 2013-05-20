from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from django import http
from models import GalleryCategory

def gallery(request, gallery=None):
    v = ""
    cats = None
    if gallery in ['bridal', 'memorial', 'original', 'other']:
        v = "gallery_%s.html" % gallery

    if gallery in ['original']:
        cats = GalleryCategory.objects.all()

    return render_to_response(v, {'cats': cats}, context_instance=RequestContext(request))

