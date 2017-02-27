# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taberna', '0010_auto_20170226_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cerveza',
            name='presentaciones',
        ),
        migrations.AddField(
            model_name='presentacion',
            name='cervezas',
            field=models.ManyToManyField(through='taberna.PresentacionCerveza', to='taberna.Cerveza'),
        ),
    ]
