from django.contrib.gis.db import models


class Diag(models.Model):
    patologia = models.CharField(max_length=200)
    count = models.IntegerField()

    class Meta:
        managed: False