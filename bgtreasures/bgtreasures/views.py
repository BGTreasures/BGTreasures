from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from django import http
from person.models import Person

def home(request):
    p = Person.objects.all
    return render_to_response('home.html', {'people':p}, context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html', {}, context_instance=RequestContext(request))

def gallery(request, gallery=None):
    v = ""
    if gallery in ['bridal', 'memorial', 'original', 'other']:
        v = "gallery_%s.html" % gallery

    return render_to_response(v, {}, context_instance=RequestContext(request))

