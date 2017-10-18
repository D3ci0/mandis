from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from mandis.models.diagnosi_model import Diagnosi
from mandis.serializers.diagnosi_serializer import Diagnosi_Serializer


@csrf_exempt
def diagnosi_list(request):
    if request.method == 'GET':
        studenti = Diagnosi.objects.all()
        serializer = Diagnosi_Serializer(studenti, many=True)
        return JsonResponse(serializer.data, safe=False)