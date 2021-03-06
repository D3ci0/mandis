from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.gis.geos import GEOSGeometry
from mandis.models.diag_model import Diag
from mandis.models.diagnosi_model import Diagnosi
from django.core.serializers import serialize
from django.db import connection

import json

@csrf_exempt
def diagnosi_list(request):
    if request.method == 'GET':
        diagnosi = Diagnosi.objects.raw('SELECT * FROM mandis_diagnosi')
        serialized = serialize('geojson', diagnosi)
        return JsonResponse(serialized, safe=False)

@csrf_exempt
def diagnosi_per_area(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        geom = body['features'][0]
        cursor = connection.cursor()

        if(geom['geometry']['type'] == 'circle'):
            cursor.execute('select patologia, COUNT(patologia) as recurrence from mandis_diagnosi where ST_Covers(ST_buffer(ST_GeographyFromText(\'POINT(%s %s)\'),%s), residenza_paziente) group by patologia order by recurrence desc limit 10',
            [geom['geometry']['coordinates'][0][0], geom['geometry']['coordinates'][0][1], geom['properties']])

        else:
            geometry = GEOSGeometry(str(geom['geometry']))
            cursor.execute('select patologia, COUNT(patologia) as recurrence from mandis_diagnosi where ST_Covers(ST_GeographyFromText(%s), residenza_paziente) group by patologia order by recurrence desc limit 10',
            [geometry.wkt])

        diag_list = []
        for row in cursor.fetchall():
            Diag(row[0], row[1])
            diag_list.append(row)

        serialized = json.dumps(diag_list)
        return JsonResponse(serialized, safe=False)

#Query Data una sorgente di inquinamento, le malattie più frequenti entro una certa distanzada essa
@csrf_exempt
def diagnosi_per_sorgente(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        geom = body['features']
        geometry = GEOSGeometry(str(geom['geometry']))
        cursor = connection.cursor()
        cursor.execute('SELECT patologia, COUNT(patologia) as recurrence FROM mandis_diagnosi WHERE ST_Distance(ST_GeographyFromText(%s), residenza_paziente) <= %s GROUP BY patologia ORDER BY recurrence desc LIMIT 10', [geometry.wkt,body['distanza']*1000])

        diag_list = []
        for row in cursor.fetchall():
            Diag(row[0], row[1])
            diag_list.append(row)

        serialized = json.dumps(diag_list)
        return JsonResponse(serialized, safe=False)

@csrf_exempt
def inserisci_diagnosi(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        features = body['features']
        features = json.loads(features)
        features = features['features']
        geom = features[0]['geometry']
        geometry = GEOSGeometry(str(geom))
        cursor = connection.cursor()
        cursor.execute('INSERT INTO mandis_diagnosi (residenza_paziente, data_diagnosi, patologia) VALUES (ST_GeographyFromText(%s), TO_DATE(%s, \'dd/mm/yyyy\'), %s)', [geometry.wkt, body['data_diagnosi'], body['patologia']])
        return HttpResponse()