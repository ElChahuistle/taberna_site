# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristicas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caracteristica', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Cerveza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('grados', models.CharField(max_length=5)),
                ('precio', models.FloatField(default=0)),
                ('on_hand', models.IntegerField(default=0)),
                ('caracteristicas', models.ManyToManyField(to='taberna.Caracteristicas')),
            ],
        ),
        migrations.CreateModel(
            name='Ceveceria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ceveceria', models.CharField(max_length=15, verbose_name='Cerveceria')),
            ],
        ),
        migrations.CreateModel(
            name='Mostrar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mostrar', models.BooleanField(default=False)),
                ('orden', models.IntegerField(default=1)),
                ('cerveza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taberna.Cerveza')),
            ],
        ),
        migrations.CreateModel(
            name='Pais_de_Origen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Pais')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='ceveceria',
            name='pais_de_origen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taberna.Pais_de_Origen'),
        ),
        migrations.AddField(
            model_name='cerveza',
            name='cerveza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taberna.Ceveceria'),
        ),
        migrations.AddField(
            model_name='cerveza',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taberna.Tipo'),
        ),
    ]