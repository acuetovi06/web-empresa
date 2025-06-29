from django.urls import path
from . import views

urlpatterns = [
    # Paths de la app services
    path('', views.services, name='services'),  # Se define en la raiz de la app services
]