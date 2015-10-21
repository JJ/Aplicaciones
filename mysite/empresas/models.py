from django.db import models

# Create your models here.


class Empresa(models.Model):
    nombre_empresa = models.CharField(max_length=200)
    correo_empresa = models.CharField(max_length=200)

class Valoracion(models.Model):
    empresa = models.ForeignKey(Empresa)
    comentario = models.CharField(max_length=200)
    puntuacion = models.IntegerField(default=0)
