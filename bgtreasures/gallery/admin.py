from django.contrib import admin
from models import *

class GalleryImageInline(admin.TabularInline):
    model = GalleryItemImage
    extra = 1

class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'item_num', 'category', 'order')
    list_filter = ['category', 'addedOn']
    search_fields = ['title', 'description']
    fieldsets = [
        (None, {'fields': ['item_num', 'title', 'category', 'description']}),
        ('Images', {'fields': ['cover', 'image', 'frame_image']}),
        ('Order', {'fields': ['order']}),
        ('Dates', {'fields': ['addedOn', 'updatedOn'], 'classes': ['collapse']}),
    ]
    inlines = [GalleryImageInline]

admin.site.register(GalleryCategory)
admin.site.register(GalleryItem, GalleryItemAdmin)
admin.site.register(GalleryItemImage)
admin.site.register(GalleryItemModifier)
