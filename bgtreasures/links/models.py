from django.db import models
import datetime

class LinkCategory(models.Model):
    title = models.CharField(max_length=50, allow_null=True)
    order = models.IntField(default=10)
    added_on = models.DateTimeField(default=datetime.datetime.now)
    updated_on = models.DateTimeField(default=datetime.datetime.now)

class LinkItem(models.Model):
    category = models.ForeignKey(LinkCategory)
    resource_title = models.CharField(max_length=50)
    resource_link = models.LinkField()
    resource_description = models.CharField(max_length=200, allow_empty=True)
    order = models.IntField(default=10)
    added_on = models.DateTimeField(default=datetime.datetime.now)
    updated_on = models.DateTimeField(default=datetime.datetime.now)
