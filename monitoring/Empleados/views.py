import json
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .logic import Empleados_logic as El
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt

def empleado_view(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id: 
            empleado_dto = El.get_empleados(id)
            empleado = serializers.serialize('json', [empleado_dto,])
            return HttpResponse(empleado, 'application/json')
        else: 
            empleados_dto = El.get_all_empleados()
            empleados = serializers.serialize('json', empleados_dto)
            return HttpResponse(empleados, 'application/json')
        
    if request.method == 'POST':
        empleado_dto = El.create_empleados(json.loads(request.body))
        empleado = serializers.serialize('json', [empleado_dto,])
        return HttpResponse(empleado, 'application/json')
