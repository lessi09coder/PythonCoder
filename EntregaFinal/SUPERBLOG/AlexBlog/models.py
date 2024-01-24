from django.db import models
from django.utils.timezone import now

# Create your models here.
class Entrada(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    cuerpo = models.TextField(max_length=400)
    imagen = models.URLField()
    autor = models.CharField(max_length=50)
    fecha = models.DateTimeField(default=now, editable=False)
    
    #Devuelve en el ADMIN el nombre:
    def __str__(self):
        return f"{self.titulo}"


    
    
