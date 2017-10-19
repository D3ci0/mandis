from django.contrib.gis.db import models

class Sorgente_puntiforme(models.Model):
    area=models.GeometryField()