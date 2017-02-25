from __future__ import unicode_literals
from django.db import models


class Tipo(models.Model):
    tipo = models.CharField(max_length=15)

    def __str__(self):
        return self.tipo


class Pais_de_Origen(models.Model):
    name = models.CharField('Pais', max_length=15)

    def __str__(self):
        return self.name

class Ceveceria(models.Model):
    ceveceria = models.CharField(
        'Cerveceria'
        , max_length=25
    )
    pais_de_origen = models.ForeignKey(Pais_de_Origen)

    def __str__(self):
        return self.ceveceria


class Caracteristica(models.Model):
    caracteristica = models.CharField(max_length=15)

    def __str__(self):
        return self.caracteristica


class Cerveza(models.Model):
    name = models.CharField(max_length=25)
    tipo = models.ForeignKey(Tipo)
    cerveceria = models.ForeignKey(Ceveceria)
    caracteristicas = models.ManyToManyField(Caracteristica)
    grados = models.CharField(max_length=5)
    precio = models.FloatField(default=0)
    on_hand = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def existencia(self):
        return self.on_hand > 0


class Mostrar(models.Model):
    cerveza = models.ForeignKey(Cerveza)
    mostrar = models.BooleanField(default=False)
    orden = models.IntegerField(default=1)

    def mostrar_cerveza(self):
        return self.cerveza.existencia()
