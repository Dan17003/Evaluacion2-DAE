from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tiempo = models.IntegerField(help_text="Tiempo en minutos")
    dificultad = models.CharField(max_length=10, choices=[('fácil', 'Fácil'), ('media', 'Media'), ('difícil', 'Difícil')])
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    ingredientes = models.ManyToManyField(Ingrediente, through='RecetaIngrediente')

    def __str__(self):
        return self.nombre

class RecetaIngrediente(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=100)

class Favorita(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
