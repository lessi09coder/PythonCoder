from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.
 
class Entrada(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    cuerpo = models.TextField(max_length=400)
    #imagen = models.ImageField('Imagen del articulo.', upload_to= 'imagenes/', max_length= 200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE) 
    #en fecha podemos usar mejor el "auto_now_add=True"
    fecha = models.DateTimeField(default=now, editable=False)
    
    #Devuelve en el ADMIN el nombre:
    def __str__(self):
        return f"{self.titulo} - {self.autor}"
