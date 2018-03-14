from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis import geos

from mandis.models.sorg_model import Sorg
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
            src = Sorgente(None, row[1], row[2], row[3], row[4])
            src_list.append(src)
      
        serialized = serialize('geojson',src_list)
        return JsonResponse(serialized, safe=False)

#Query che ritorna le sorgenti di inquinamento più vicine all'area geografica in input
@csrf_exempt
def sorgenti_per_area(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        geom = body['features'][0]

        if(geom['geometry']['type'] == 'circle'):
            center = geos.Point(geom['geometry']['coordinates'][0][0],geom['geometry']['coordinates'][0][1])
            center.srid = 4326
            radius = geom['properties']
            geometry = center.buffer((radius/40000000)*360)

        else:
            geometry = GEOSGeometry(str(geom['geometry']))

        cursor = connection.cursor()
        cursor.execute('SELECT *, ST_Distance(area, ST_GeographyFromText(%s)) as dist FROM mandis_sorgenti ORDER BY dist LIMIT 10',[geometry.wkt])

        sorgenti = []
        for row in cursor.fetchall():
            src = Sorg(None, row[1], row[2], row[3], row[4], row[5])
            sorgenti.append(src)

        serialized = serialize('geojson', sorgenti)
        return JsonResponse(serialized, safe=False)