from rest_framework import serializers
from mandis.models.diagnosi_model import Diagnosi

class Diagnosi_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Diagnosi
        fields=('id','patologia','data_diagnosi','residenza_paziente')