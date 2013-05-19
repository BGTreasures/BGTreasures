from django import forms
from django.db import models

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(max_length=500)

class HomeCarousel(models.Model):
    name = models.CharField(max_length=50)
    alt = models.CharField(max_length=50)
    descrip = models.CharField(max_length=50)
