from django.db import models

# Create your models here.
class Alunos(models.Model):
    nome = models.CharField(max_length=150)
    curso = models.CharField(max_length=100)
    dataInicio = models.IntegerField()
    presencas = models.IntegerField()
    aulasRestantes = models.IntegerField()