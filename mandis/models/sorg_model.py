from django.contrib.gis.db import models


class Sorg(models.Model):
    area = models.GeometryField(geography=True)
    raggio = models.FloatField()
    data_inizio = models.DateTimeField()
    data_fine = models.DateTimeField()
    distanza = models.FloatField()


    class Meta:
        managed: False