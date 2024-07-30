from django.db import models
from consultas.models import Estudiantes
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    numero = models.IntegerField(default=0)
    foreign = models.ForeignKey(
        Estudiantes, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
