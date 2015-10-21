import datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class Empresas (models.Model):
	nombre = models.CharField (max_length=200)
	correo = models.CharField (max_length=200)
	#fecha_visita = models.DateField ('Fecha visita') #'%Y-%m-%d %H:%M:%S'
	

	def __unicode__(self):
		return self.nombre

	#def fue_visitado_recientemente(self):
		#return self.fecha_visita >= timezone.now () - datetime.timedelta (days=1)


class Valoracion(models.Model):
	empresa = models.ForeignKey (Empresas)
	comentario = models.CharField (max_length=200)
	puntuacion = models.IntegerField (default=0)
	

	def __unicode__(self):
		return self.comentario
