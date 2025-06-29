from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='services', verbose_name='Imagen')  # The 'upload_to' parameter specifies the directory within MEDIA_ROOT where the file will be stored.
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')   # Automatically set the field to now when the object is first created.
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')   # Automatically set the field to now every time the object is saved.
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-created']     # Order by created date, newest first

    def __str__(self):
        return self.title