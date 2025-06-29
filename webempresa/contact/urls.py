from django.urls import path
from . import views

urlpatterns = [
    # Paths de la app core
    path('', views.contact, name='contact'),
]
