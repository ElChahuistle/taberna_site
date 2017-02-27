# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.db import models


class Tipo(models.Model):
    tipo = models.CharField(max_length=15)

    def __str__(self):
        return self.tipo


class Pais_de_Origen(models.Model):
    name = models.CharField(
        max_length=15
        , verbose_name='Pais'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pais de Origen'
        verbose_name_plural = 'Paises de Origen'


class Ceveceria(models.Model):
    ceveceria = models.CharField(max_length=25)
    pais_de_origen = models.ForeignKey(Pais_de_Origen)

    def __str__(self):
        return self.ceveceria


class Caracteristica(models.Model):
    caracteristica = models.CharField(max_length=15)

    def __str__(self):
        return self.caracteristica

    class Meta:
        verbose_name = 'Caracteristica'
        verbose_name_plural = 'Caracteristicas'


class Presentacion(models.Model):
    PRESENTACIONES = (
        ('BA', 'Barril')
        , ('BO', 'Botella')
    )
    presentacion = models.CharField(max_length=2, choices=PRESENTACIONES)

    def __str__(self):
        return self.presentacion


class Cerveza(models.Model):
    name = models.CharField(max_length=25)
    tipo = models.ForeignKey(Tipo)
    cerveceria = models.ForeignKey(Ceveceria)
    caracteristicas = models.ManyToManyField(Caracteristica)
    grados = models.CharField(max_length=5)
    presentaciones = models.ManyToManyField(Presentacion, through='PresentacionCerveza')

    def __str__(self):
        return self.name

    def existencia(self):
        return self.disponible > 0

    existencia.boolean = True
    existencia.verbose_name = 'Hay Disponile?'


class PresentacionCerveza(models.Model):
    cerveza = models.ForeignKey(Cerveza, on_delete=models.CASCADE)
    presentacion = models.ForeignKey(Presentacion, on_delete=models.CASCADE)
    precio = models.FloatField(default=0)
    disponible = models.FloatField(default=0)


class Mostrar(models.Model):
    cerveza = models.OneToOneField(Cerveza, primary_key=True)
    mostrar = models.BooleanField(default=False)
    orden = models.IntegerField(default=1)

    def mostrar_cerveza(self):
        return self.cerveza.existencia()

