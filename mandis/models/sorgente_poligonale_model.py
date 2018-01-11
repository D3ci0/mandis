from django.contrib.gis.db import models

class Sorgente_poligonale(models.Model):
    area=models.GeometryField(geography=True)
    data_inizio=models.DateTimeField()
    data_fine=models.DateTimeField()