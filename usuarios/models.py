from django.db import models

# Create your models here.
class Usuarios(models.Model):

    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
