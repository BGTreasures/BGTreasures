from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import http

def links(request):
    descriptions = range(0,3)
    links = range(1,3)
    return render_to_response('links.html', {'descriptions': descriptions, 'links': links}, context_instance=RequestContext(request))

