from django.contrib.gis.db import models

class Sorgente_lineare(models.Model):
    area=models.GeometryField()