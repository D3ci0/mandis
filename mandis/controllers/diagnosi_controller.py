from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from mandis.models.diagnosi_model import Diagnosi
from mandis.models.sorgente_model import Sorgente
from mandis.serializers.diagnosi_serializer import Diagnosi_Serializer
from mandis.serializers.sorgente_serializer import Sorgente_Serializer


@csrf_exempt
def diagnosi_list(request):
    if request.method == 'GET':
        diagnosi = Diagnosi.objects.all()
        serializer = Diagnosi_Serializer(diagnosi, many=True)
        return JsonResponse(serializer.data, safe=False)
    
@csrf_exempt
def sorgenti_list(request):
    if request.method == 'GET':
        sorgenti= Sorgente.objects.all()
        serializer = Sorgente_Serializer(sorgenti, many=True)
        return JsonResponse(serializer.data, safe=False)