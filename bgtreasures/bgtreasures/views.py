from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from django import http

def home(request):
    return render_to_response('home.html', {}, context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html', {}, context_instance=RequestContext(request))

def gallery(request, gallery=None):
    v = ""
    if gallery == "bridal":
        v = "%s_bridal.html" % "gallery"
    elif gallery == "memorial":
        v = "%s_memorial.html" % "gallery"
    elif gallery == "original_art":
        v = "%s_original_art.html" % "gallery"
    elif gallery == "other":
        v = "%s_other.html" % "gallery"
    return render_to_response(v, {}, context_instance=RequestContext(request))

