from django.contrib import admin
from models import GalleryCategory, GalleryItem, GalleryItemModifier

admin.site.register(GalleryCategory)
admin.site.register(GalleryItem)
admin.site.register(GalleryItemModifier)