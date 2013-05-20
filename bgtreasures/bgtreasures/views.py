from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
# from django.http import HttpResponseRedirect

from django import http

from models import ContactForm

def home(request):
    imgs = []
    return render_to_response('home.html', {'imgs': imgs}, context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html', {}, context_instance=RequestContext(request))

def supplies(request):
    return render_to_response('supplies.html', {}, context_instance=RequestContext(request))

def shows(request):
    return render_to_response('shows.html', {}, context_instance=RequestContext(request))

def links(request):
    return render_to_response('links.html', {}, context_instance=RequestContext(request))

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            message = form.cleaned_data['message']

            recipients = ['email@email.com']

            from django.core.mail import send_mail
            send_mail("subject", message, sender, recipients)
            return HttpResponseRedirect('/contact_success/')
    else:
        form = ContactForm()

    return render_to_response('contact.html', {'form': form}, context_instance=RequestContext(request))

def contact_success(request):
    return render_to_response('contact_success.html', {}, context_instance=RequestContext(request))
