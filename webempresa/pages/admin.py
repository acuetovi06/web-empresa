from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("title", "order", "created", "updated")
    
admin.site.register(Page, PageAdmin)