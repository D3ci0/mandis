from django.contrib.gis.db import models

class Sorgente(models.Model):    
    area=models.GeometryField(geography=True)
    raggio=models.FloatField();
    
    class Meta:
        managed:False
        db_table='mandis_sorgenti'