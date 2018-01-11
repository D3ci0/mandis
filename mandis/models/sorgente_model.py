from django.contrib.gis.db import models

class Sorgente(models.Model):    
    area=models.GeometryField(geography=True)
    raggio=models.FloatField()
    data_inizio=models.DateTimeField()
    data_fine=models.DateTimeField()
    
    class Meta:
        managed:False
        db_table='mandis_sorgenti'