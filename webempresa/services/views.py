from django.shortcuts import render
from .models import Service  # Import the Service model to use it in the view

# Create your views here.
def services(request):
    services = Service.objects.all()  # Retrieve all services from the database
    return render(request, 'services/services.html', {'services': services})  # Render the portfolio template with the projects context
