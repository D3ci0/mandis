from django.contrib.gis.db import models

class Sorgente(models.Model):
    area=models.GeometryField(geography=True)
    tipologia=models.IntegerField()