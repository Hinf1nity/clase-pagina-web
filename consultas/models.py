from django.db import models

# Create your models here.


class Estudiantes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    carnet = models.IntegerField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre
