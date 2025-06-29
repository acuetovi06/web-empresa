from django.urls import path
from . import views

urlpatterns = [
    # Paths de la app core
    path('', views.blog, name='blog'),
    # <category_id> es un parámetro dinámico que se pasará a la vista category
    # int:category_id indica que el parámetro es un número entero
    # Si no se indica, Django lo detecta como una cadena de caracteres
    path('category/<int:category_id>/', views.category, name='category'),
]