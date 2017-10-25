from django.contrib.gis.db import models

class Sorgente_poligonale(models.Model):
    area=models.GeometryField(geography=True)