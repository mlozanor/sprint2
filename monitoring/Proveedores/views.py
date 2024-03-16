import json
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .logic import proveedores_logic as pl
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt

def proveedor_view(request):
    
        if request.method == 'GET':
            id = request.GET.get('id', None)
            if id: 
                documento_dto = pl.get_proveedores(id)
                documento = serializers.serialize('json', [documento_dto,])
                return HttpResponse(documento, 'application/json')
            else: 
                documentos_dto = pl.get_all_proveedores()
                documentos = serializers.serialize('json', documentos_dto)
                return HttpResponse(documentos, 'application/json')
            
        if request.method == 'POST':
            documento_dto = pl.create_proveedores(json.loads(request.body))
            documento = serializers.serialize('json', [documento_dto,])
            return HttpResponse(documento, 'application/json')