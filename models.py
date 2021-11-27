from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    camada = models.IntegerField

class Estudientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechadeentrega = models.DateField()
    entregado = models.BooleanField()
    