from django.contrib.gis.db import models

class Diagnosi(models.Model):
    patologia= models.CharField(max_length=200)
    data_diagnosi=models.DateTimeField()
    residenza_paziente=models.PointField(srid=4326)
    