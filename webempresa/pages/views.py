from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.
def page(request, page_id, page_slug):
    # Get the page object with the given ID or return a 404 error if not found
    page = get_object_or_404(Page, id=page_id)
    
    # Render the 'page.html' template with the page object as context
    return render(request, "pages/sample.html", {"page": page})
