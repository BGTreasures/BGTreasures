from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import http
from django.core.urlresolvers import reverse

from models import ContactForm
from django.core.mail import EmailMessage
from bgtreasures import settings

def contact(request):
    send_error = None
    recipient_email = settings.EMAIL_TO
    if request.method == 'POST':
        send_to = []
        for manager in settings.MANAGERS:
            name, email = manager
            send_to.append(email)

        form = ContactForm(request.POST)
        if form.is_valid():
            data = {'name':form.cleaned_data['name'], 'email': form.cleaned_data['email'], 'message': form.cleaned_data['message']}
            try:
                email_message = settings.EMAIL_TEMPLATE.format(**data)
                bcc = [settings.ADMIN_EMAIL_TO]
                email_split = recipient_email.split('@')
                from_email = "".join((email_split[0], "+", "@", email_split[1]))
                msg = EmailMessage(settings.EMAIL_SUBJECT, email_message, from_email, send_to, bcc, 
                        headers = {'Reply-To': data['email']})
                msg.send()
                return HttpResponseRedirect(reverse('contact_success'))
            except:
                send_error = "You contact submission cannot be sent at this time. Send an email to %s and let them know of this error" % (recipient_email)

            form = ContactForm({'name': data['name'], 'email': data['email'], 'message': data['message']})
    else:
        form = ContactForm()

    return render_to_response('contact.html', {'form': form, 'send_status': send_error, 'email': recipient_email}, context_instance=RequestContext(request))

def contact_success(request):
    return render_to_response('contact_success.html', {}, context_instance=RequestContext(request))
