from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from mandis.models.diagnosi_model import Diagnosi
from mandis.models import *
from mandis.serializers.diagnosi_serializer import Diagnosi_Serializer
from django.core.serializers import serialize


@csrf_exempt
def diagnosi_list(request):
    if request.method == 'GET':
        diagnosi = Diagnosi.objects.raw('SELECT * FROM mandis_diagnosi')
        serialized = serialize('geojson', diagnosi)
        return JsonResponse(serialized, safe=False)
