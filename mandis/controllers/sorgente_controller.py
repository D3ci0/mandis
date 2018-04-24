from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.contrib.gis.geos import GEOSGeometry

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
        cursor = connection.cursor()

        if(geom['geometry']['type'] == 'circle'):
            cursor.execute('SELECT *, ST_Distance(area, ST_buffer(ST_GeographyFromText(\'POINT(%s %s)\'),%s)) as dist FROM mandis_sorgenti ORDER BY dist LIMIT 10', [geom['geometry']['coordinates'][0][0],geom['geometry']['coordinates'][0][1], geom['properties']])

        else:
            geometry = GEOSGeometry(str(geom['geometry']))
            cursor.execute('SELECT *, ST_Distance(area, ST_GeographyFromText(%s)) as dist FROM mandis_sorgenti ORDER BY dist LIMIT 10', [geometry.wkt])

        sorgenti = []
        for row in cursor.fetchall():
            src = Sorg(None, row[1], row[2], row[3], row[4], row[5])
            sorgenti.append(src)

        serialized = serialize('geojson', sorgenti)
        return JsonResponse(serialized, safe=False)

@csrf_exempt
def inserisci_sorgente(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        features = body['features']
        features = json.loads(features)
        features = features['features']
        geom = features[0]['geometry']
        cursor = connection.cursor()
        if(geom['type'] == 'circle'):
            cursor.execute('INSERT INTO mandis_sorgente_circolare (area, data_inizio, data_fine) VALUES (ST_buffer(ST_GeographyFromText(\'POINT(%s %s)\'), %s), TO_DATE(%s, \'dd/mm/yyyy\'), TO_DATE(%s, \'dd/mm/yyyy\'))', [geom['coordinates'][0][0], geom['coordinates'][0][1], features[0]['properties'], body['data_inizio'], body['data_fine']])
        elif(geom['type'] == 'linestring'):
            geometry = GEOSGeometry(str(geom))
            cursor.execute('INSERT INTO mandis_sorgente_lineare (area, data_inizio, data_fine) VALUES (ST_GeographyFromText(%s), TO_DATE(%s, \'dd/mm/yyyy\'), TO_DATE(%s, \'dd/mm/yyyy\'))', [geometry.wkt, body['data_inizio'], body['data_fine']])
        else:
            geometry = GEOSGeometry(str(geom))
            cursor.execute('INSERT INTO mandis_sorgente_poligonale (area, data_inizio, data_fine) VALUES (ST_GeographyFromText(%s), TO_DATE(%s, \'dd/mm/yyyy\'), TO_DATE(%s, \'dd/mm/yyyy\'))', [geometry.wkt, body['data_inizio'], body['data_fine']])
        return HttpResponse()