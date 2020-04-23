import uuid
from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='Titulo', max_length=200)
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to='project')
    url = models.URLField(verbose_name='Dirección WEB',blank=True,null=True)
    created = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] #ordenado de descendente - 

