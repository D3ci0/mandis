from rest_framework import serializers
from mandis.models.sorgente_model import Sorgente

class Sorgente_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Sorgente
        fields=('id','area','tipologia')