from django.db import models
from django.contrib.auth.models import User

TIPO_CHOICES=[("S","suspencion de actividades"),
              ("C","Suspencion de clase"),
              ("I","Informacion")]

class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='myapp/static/myapp/img/')
    def __str__(self) -> str:
        return self.nombre
    
class Comunicado(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo=models.CharField(max_length=255)
    detalle = models.CharField(max_length=255)
    detalle_corto=models.CharField(max_length=160)
    tipo=models.CharField(max_length=50,choices=TIPO_CHOICES)
    entidad= models.ForeignKey(Entidad,on_delete=models.CASCADE)
    visible = models.BooleanField()
    fecha_publicacion= models.DateTimeField()
    fecha_ultima_publicacion=models.DateTimeField()
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comunicados_publicados')
    modificado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comunicados_modificados')
    def __str__(self) -> str:
        return self.titulo

# Create your models here.
