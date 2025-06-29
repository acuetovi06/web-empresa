from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')  # Fields that should be read-only in the admin interface

admin.site.register(Service, ServiceAdmin)  # Register the Project model with the custom admin interface