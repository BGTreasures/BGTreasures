from django.contrib import admin
from models import *
from forms import *

class LinkCategoryItemInline(admin.StackedInline):
    model = LinkItem
    extra = 1
    form = LinkItemAdminForm

class LinkCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'added_on', 'updated_on', 'get_links')
    list_filter = ['title']
    search_fields = ['title', 'linkitem__resource_title']
    fieldsets = [
        (None, {'fields': ['title', 'visible']}),
        ('Order', {'fields': ['order']}),
        ('Dates', {'fields': ['added_on', 'updated_on'], 'classes': ['collapse']}),
    ]
    inlines = [LinkCategoryItemInline]

    def get_links(self, link_cat):
        return ', '.join([link.resource_title for link in link_cat.linkitem_set.all()])
    get_links.short_description = 'Links'

admin.site.register(LinkCategory, LinkCategoryAdmin)
