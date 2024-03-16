from ..models import Productos

def get_all_productos():
    return Productos.objects.all()

def get_productos(productos_pk):
    return Productos.objects.get(pk=productos_pk)