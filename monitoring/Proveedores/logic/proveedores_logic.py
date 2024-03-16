from ..models import Proveedores

def get_all_proveedores():
    return Proveedores.objects.all()

def get_proveedores(proveedores_pk):
    return Proveedores.objects.get(pk=proveedores_pk)