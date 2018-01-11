from rest_framework import serializers
from mandis.models.sorgente_lineare_model import Sorgente_lineare

class Sorgente_lineare_serializer(serializers.ModelSerializer):
    class Meta:
        model=Sorgente_lineare
        fields=('id','area', 'data inizio', 'data fine')