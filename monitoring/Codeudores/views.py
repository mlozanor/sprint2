import json
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .logic import codeudores_logic as Cdl
from django.views.decorators.csrf import csrf_exempt

def codeudor_view(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id: 
            codeudor_dto = Cdl.get_codeudores(id)
            codeudor = serializers.serialize('json', [codeudor_dto,])
            return HttpResponse(codeudor, 'application/json')
        else: 
            codeudores_dto = Cdl.get_all_codeudores()
            codeudores = serializers.serialize('json', codeudores_dto)
            return HttpResponse(codeudores, 'application/json')
        
    if request.method == 'POST':
        codeudor_dto = Cdl.create_codeudor(json.loads(request.body))
        codeudor = serializers.serialize('json', [codeudor_dto,])
        return HttpResponse(codeudor, 'application/json')


# Create your views here.
