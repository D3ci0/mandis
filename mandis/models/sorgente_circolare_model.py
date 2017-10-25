from django.contrib.gis.db import models

class Sorgente_circolare(models.Model):
    area=models.GeometryField(geography=True)
    raggio=models.FloatField();