from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from mandis.models.sorgente_model import Sorgente
from django.db import connection
import json

@csrf_exempt
def sorgenti_list(request):
    if request.method == 'GET':
        sorgenti = Sorgente.objects.raw('SELECT * FROM mandis_sorgenti')
        serialized = serialize('geojson',sorgenti)
        return JsonResponse(serialized, safe=False)
    
@csrf_exempt 
def sorgenti_per_diagnosi(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        cursor = connection.cursor()
        cursor.execute('select * from mandis_sorgenti, ST_Distance(mandis_sorgenti.area, ST_GeographyFromText(\'POINT(%s %s)\')) as distance where distance < %s order by distance limit 10 ',
                       [body['point'][0],body['point'][1],body['distanza']*1000])
        src_list= []
        for row in cursor.fetchall():
            src = Sorgente(None, row[1], row[2])
            src_list.append(src)
      
        serialized = serialize('geojson',src_list)
        return JsonResponse(serialized, safe=False)