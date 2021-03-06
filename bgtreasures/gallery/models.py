from django.db import models
import datetime

class GalleryCategory(models.Model):
    title = models.CharField(max_length=50)
    addedOn = models.DateTimeField(default=datetime.datetime.now)
    updatedOn = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.title

class GalleryItem(models.Model):
    title = models.CharField(max_length=50)
    item_num = models.IntegerField()
    category = models.ForeignKey(GalleryCategory)
    cover = models.CharField(max_length=80)
    image = models.CharField(max_length=80)
    frame_image = models.CharField(max_length=80)
    order = models.IntegerField(default=100)
    description = models.TextField()
    addedOn = models.DateTimeField(default=datetime.datetime.now)
    updatedOn = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return "(%s): %s" % (self.category.title, self.title)

    class Meta:
        ordering = ['category__id', 'order']

class GalleryItemImage(models.Model):
    item = models.ForeignKey(GalleryItem)
    image = models.CharField(max_length=255)
    order = models.SmallIntegerField(default=100)

    def __unicode__(self):
        return "(%s): %s" % (self.item.title, self.image)

    class Meta:
        ordering = ['item__id', 'order']

class GalleryItemModifier(models.Model):
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    order = models.IntegerField(default=100)
    item = models.ForeignKey(GalleryItem)

    def __unicode__(self):
        return "(%s): %s=%s" % (self.item.title, self.title, self.value)

    class Meta:
        ordering = ['item__id', 'order']
