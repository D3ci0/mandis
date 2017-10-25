from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from mandis.models.sorgente_model import Sorgente


@csrf_exempt
def sorgenti_list(request):
    if request.method == 'GET':
        sorgenti = Sorgente.objects.raw('SELECT * FROM mandis_sorgenti')
        serialized = serialize('geojson',sorgenti)
        return JsonResponse(serialized, safe=False)