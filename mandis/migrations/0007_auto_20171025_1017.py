# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 10:17
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandis', '0006_auto_20171023_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sorgente_circolare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', django.contrib.gis.db.models.fields.GeometryField(geography=True, srid=4326)),
                ('raggio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Sorgente_lineare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', django.contrib.gis.db.models.fields.GeometryField(geography=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Sorgente_poligonale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', django.contrib.gis.db.models.fields.GeometryField(geography=True, srid=4326)),
            ],
        )
    ]
