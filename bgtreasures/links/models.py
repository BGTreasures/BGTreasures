from django.db import models
import datetime

class LinkCategory(models.Model):
    title = models.CharField(max_length=50, unique=True, null=True)
    order = models.IntegerField(default=10)
    added_on = models.DateTimeField(default=datetime.datetime.now)
    updated_on = models.DateTimeField(default=datetime.datetime.now)

class LinkItem(models.Model):
    category = models.ForeignKey(LinkCategory)
    resource_title = models.CharField(max_length=50)
    resource_url = models.URLField()
    resource_description = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=10)
    added_on = models.DateTimeField(default=datetime.datetime.now)
    updated_on = models.DateTimeField(default=datetime.datetime.now)


    def __unicode__(self):
        return str(self.resource_title)
