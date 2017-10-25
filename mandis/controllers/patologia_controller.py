from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
import json

@csrf_exempt
def patologie_list(request):
    if request.method == 'GET':
        lista_patologie = ["Aneurisma","Ictus", "Infarto", "Soffio al cuore", "Bradicardia","Ischemia","Pericardite","Asma","Sarcoidosi","Pleurite","Cistite","Calcolosi renale","Cirrosi","Epatite","Ulcera","Ernia iatale","Dispepsia","Poliposi","Morbo di Crohn","Pancreatite"]
        serialized = json.dumps(lista_patologie)
        return JsonResponse(serialized, safe=False)