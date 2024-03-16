import json
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .logic import clientes_logic as cl
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def clientes_view(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id: 
            cliente_dto = cl.get_clientes(id)
            cliente = serializers.serialize('json', [cliente_dto,])
            return HttpResponse(cliente, 'application/json')
        else: 
            clientes_dto = cl.get_all_clientes()
            clientes = serializers.serialize('json', clientes_dto)
            return HttpResponse(clientes, 'application/json')
        
    if request.method == 'POST':
        cliente_dto = cl.create_cliente(json.loads(request.body))
        cliente = serializers.serialize('json', [cliente_dto,])
        return HttpResponse(cliente, 'application/json')