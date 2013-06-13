from django.contrib import admin
from django.forms import *
from models import *

class LinkItemAdminForm(ModelForm):
    class Meta:
        model = LinkItem
        widgets = {
            'resource_description': admin.widgets.AdminTextareaWidget,
        }
