# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 10:05
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mandis', '0004_auto_20171019_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorgente',
            name='area',
            field=django.contrib.gis.db.models.fields.GeometryField(geography=True, srid=4326),
        ),
    ]
