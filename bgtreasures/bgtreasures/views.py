from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from django import http

def home(request):
    return render_to_response('home.html', {}, context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html', {}, context_instance=RequestContext(request))

def supplies(request):
    return render_to_response('supplies.html', {}, context_instance=RequestContext(request))

def shows(request):
    return render_to_response('shows.html', {}, context_instance=RequestContext(request))

def links(request):
    return render_to_response('links.html', {}, context_instance=RequestContext(request))

def contact(request):
    return render_to_response('contact.html', {}, context_instance=RequestContext(request))

def gallery(request, gallery=None):
    v = ""
    if gallery in ['bridal', 'memorial', 'original', 'other']:
        v = "gallery_%s.html" % gallery

    return render_to_response(v, {}, context_instance=RequestContext(request))

