from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField (max_length=40)
    camada = models.IntegerField ()

    def __str__(self):
        return f"Nombre: {self.nombre}    Camada: {self.camada}"  
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido} (DNI: {self.dni})"
    
class Profesores(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido} (DNI: {self.dni})"