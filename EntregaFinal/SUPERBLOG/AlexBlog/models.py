from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, default='SOME STRING')
    last_name = models.CharField(max_length=50, default='SOME STRING')
    password = models.CharField(max_length=50, default='SOME STRING')
        
    def siExiste(self):
        if Usuario.objects.filter(username = self.username):
            return True
        return False
    
    def __str__(self):
        return f"{self.username}"


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


    
    
