from django.db import models
from django import forms
import datetime

class LinkCategory(models.Model):
    title = models.CharField(max_length=50, unique=True, blank=True)
    order = models.IntegerField(default=10)
    added_on = models.DateTimeField(default=datetime.datetime.now)
    visible = models.BooleanField(default=True)
    updated_on = models.DateTimeField(default=datetime.datetime.now)

    def visible_items(self):
        return self.linkitem_set.filter(visible=True).order_by("order")

    def __unicode__(self):
        return str(self.title)

class LinkItem(models.Model):
    category = models.ForeignKey(LinkCategory)
    resource_title = models.CharField(max_length=50)
    resource_url = models.CharField(max_length=100)
    resource_description = models.CharField(max_length=1000, blank=True)
    order = models.IntegerField(default=10)
    visible = models.BooleanField(default=True)
    added_on = models.DateTimeField(default=datetime.datetime.now)
    updated_on = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return str(self.resource_title)
