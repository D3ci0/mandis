from rest_framework import serializers
from mandis.models.sorgente_model import Sorgente

class Sorgente_serializer(serializers.ModelSerializer):
    class Meta:
        model=Sorgente
        fields=('id','area','raggio','data inizio', 'data fine')