from django import template
from pages.models import Page

register = template.Library()

@register.simple_tag
def get_page_list():
    """
    Returns a list of all pages in the database.
    """
    pages = Page.objects.all()
    return pages