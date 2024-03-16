from ..models import Clientes

def get_all_clientes():
    return Clientes.objects.all()

def get_clientes(cliente_pk):
    return Clientes.objects.get(pk=cliente_pk)