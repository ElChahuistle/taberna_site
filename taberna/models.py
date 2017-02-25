from __future__ import unicode_literals
# -*- coding: utf-8 -*-
import os, sys
from django.db import models


class Tipo(models.Model):
    tipo = models.CharField(max_length=15)


class Ceveceria(models.Model):
    ceveceria = models.CharField(
        'Cerveceria'
        , max_length=15
    )


class Pais_de_Origen(models.Model):
    name = models.CharField('Pais', max_length=15)


class Cerveza(models.Model):
    name = models.CharField(max_length=25)
    tipo = models.ForeignKey(Tipo)
    cerveza = models.ForeignKey(Ceveceria)
    grados = models.CharField(max_length=5)
    precio = models.FloatField(default=0)
    existencia = models.IntegerField(default=0)
