import json
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .logic import solicitudes_logic as sl
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt

def solicitudes_view(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id: 
            solicitud_dto = sl.get_solicitudes(id)
            solicitud = serializers.serialize('json', [solicitud_dto,])
            return HttpResponse(solicitud, 'application/json')
        else: 
            solicitudes_dto = sl.get_all_solicitudes()
            solicitudes = serializers.serialize('json', solicitudes_dto)
            return HttpResponse(solicitudes, 'application/json')
        
    if request.method == 'POST':
        solicitud_dto = sl.create_solicitudes(json.loads(request.body))
        solicitud = serializers.serialize('json', [solicitud_dto,])
        return HttpResponse(solicitud, 'application/json')