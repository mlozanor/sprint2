from ..models import Solicitudes

def get_all_solicitudes():
    return Solicitudes.objects.all()

def get_solicitudes(solicitudes_pk):
    return Solicitudes.objects.get(pk=solicitudes_pk)