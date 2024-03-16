from ..models import Empleados

def get_all_empleados():
    return Empleados.objects.all()

def get_empleados(empleados_pk):
    return Empleados.objects.get(pk=empleados_pk)