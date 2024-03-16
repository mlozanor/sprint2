import json
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .logic import Documentos_logic as Dl
from django.views.decorators.csrf import csrf_exempt    

@csrf_exempt

def documento_view(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id: 
            documento_dto = Dl.get_documentos(id)
            documento = serializers.serialize('json', [documento_dto,])
            return HttpResponse(documento, 'application/json')
        else: 
            documentos_dto = Dl.get_all_documentos()
            documentos = serializers.serialize('json', documentos_dto)
            return HttpResponse(documentos, 'application/json')
        
    if request.method == 'POST':
        documento_dto = Dl.create_documentos(json.loads(request.body))
        documento = serializers.serialize('json', [documento_dto,])
        return HttpResponse(documento, 'application/json')

# Create your views here.
