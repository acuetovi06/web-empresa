from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    # Slugfield is a short label for something, containing only letters, numbers, underscores or hyphens.
    # It is used to create a URL-friendly version of the name.
    title = models.CharField(verbose_name="Titulo", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True) 
    updated = models.DateTimeField(verbose_name="Fecha de edición", auto_now=True)
    
    class Meta:
        verbose_name = "pagina"
        verbose_name_plural = "paginas"
        ordering = ['order', "title"]

    def __str__(self):
        return self.title