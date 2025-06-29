from django.contrib import admin
from .models import Category, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created",
        "updated",
    )  # Fields that should be read-only in the admin interface


class PostAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created",
        "updated",
    )  # Fields that should be read-only in the admin interface
    list_display = (
        "title",
        "author",
        "published",
        "post_categories"
    )  # Fields to display in the list view
    ordering = ("author", "published")  # Fields to order the list view
    search_fields = (
        "title",
        "content",
        "author__username",
        "categories__name",
    )  # Fields to search in the list view
    date_hierarchy = "published"  # Field to use for date hierarchy in the list view
    list_filter = (
        "author__username",
        "published",
        "categories",
    )  # Fields to filter the list view

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"  # Short description for the custom field

admin.site.register(
    Category, CategoryAdmin
)  # Register the Category model with the custom admin interface
admin.site.register(
    Post, PostAdmin
)  # Register the Post model with the custom admin interface
