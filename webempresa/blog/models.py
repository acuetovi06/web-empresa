from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created']

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de Publicación', default=now)  # Default to now when the object is created
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)  # The 'upload_to' parameter specifies the directory within MEDIA_ROOT where the file will be stored.
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)  # Foreign key to the User model
    categories = models.ManyToManyField(Category, verbose_name='Categorías', blank=True, related_name='get_posts')  # Many-to-many relationship with Category model
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')   # Automatically set the field to now when the object is first created.
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')   # Automatically set the field to now every time the object is saved.

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']

    def __str__(self):
        return self.title