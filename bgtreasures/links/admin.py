from django.contrib import admin
from models import *

class LinkCategoryItemInline(admin.TabularInline):
    model = LinkItem
    extra = 3

class LinkCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'added_on', 'updated_on', 'get_links')
    list_filter = ['title']
    search_fields = ['title', 'linkitem__resource_title']
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Order', {'fields': ['order']}),
        ('Dates', {'fields': ['added_on', 'updated_on'], 'classes': ['collapse']}),
    ]
    inlines = [LinkCategoryItemInline]

    def get_links(self, link_cat):
        return ', '.join([link.resource_title for link in link_cat.linkitem_set.all()])
    get_links.short_description = 'Links'

admin.site.register(LinkCategory, LinkCategoryAdmin)
