# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 15:26
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandis', '0002_sorgente_lineare'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sorgente_poligonale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Sorgente_puntiforme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
            ],
        ),
    ]