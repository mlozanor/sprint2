import json
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .logic import Banco_logic as bl
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def banco_view(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id: 
            banco_dto = bl.get_bancos(id)
            banco = serializers.serialize('json', [banco_dto,])
            return HttpResponse(banco, 'application/json')
        else: 
            bancos_dto = bl.get_all_bancos()
            bancos = serializers.serialize('json', bancos_dto)
            return HttpResponse(bancos, 'application/json')
        
    if request.method == 'POST':
        banco_dto = bl.create_banco(json.loads(request.body))
        banco = serializers.serialize('json', [banco_dto,])
        return HttpResponse(banco, 'application/json')

