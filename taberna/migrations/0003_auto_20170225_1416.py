# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taberna', '0002_auto_20170225_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ceveceria',
            name='ceveceria',
            field=models.CharField(max_length=25, verbose_name='Cerveceria'),
        ),
    ]
