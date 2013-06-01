from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import http
from django.core.urlresolvers import reverse

from models import ContactForm
from django.core.mail import send_mail
from bgtreasures import settings

def contact(request):
    send_error = None
    recipient_name, recipient_email = settings.MANAGERS[0]
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            message = form.cleaned_data['message']

            if name and sender and message:
                try:
                    send_mail(settings.EMAIL_SUBJECT, message, sender, [recipient_email])
                    contact_success = reverse('contact_success')
                    return HttpResponseRedirect(contact_success)
                except:
                    send_error = "You contact submission cannot be sent at this time. Send an email to %s and let them know of this error" % (recipient)

            form = ContactForm({'name': name, 'email': sender, 'message': message})
    else:
        form = ContactForm()

    return render_to_response('contact.html', {'form': form, 'send_status': send_error, 'email': recipient_email}, context_instance=RequestContext(request))

def contact_success(request):
    return render_to_response('contact_success.html', {}, context_instance=RequestContext(request))
