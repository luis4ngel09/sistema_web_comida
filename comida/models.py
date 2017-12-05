from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class comidas (models.Model):
	author         = models.ForeignKey('auth.User')
	nombre         = models.CharField(max_length=200)
	descripcion    = models.TextField()
	costo          = models.IntegerField()
	imagen        = models.ImageField(upload_to='comida/images/')
	fecha_creacion = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.fecha_creacion = timezone.now()
		self.save()

	def __str__(self):
		return self.nombre

class usuarios(models.Model):
	nombre      = models.CharField(max_length=200)
	password    = models.CharField(max_length=200)
	#email		= models.EmailField(max_length=200)
	descripcion = models.TextField()
	imagen        = models.ImageField(upload_to='comida/images/')
	tipo_usuario= models.CharField(max_length=200)

	def __str__(self):
		return self.nombre

class pedidos(models.Model):
	#author=models.ForeignKey('auth.User')
	comida_id = models.ForeignKey(comidas, on_delete=models.CASCADE)
	#usuario_id     = models.ForeignKey(usuarios,on_delete=models.CASCADE)
	nombre         = models.CharField(max_length=200)
	cantidad       = models.IntegerField()
	descripcion    = models.TextField()
	fecha_creacion = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.fecha_creacion = timezone.now()
		self.save()

	def __str__(self):
		return self.nombre