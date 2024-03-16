from ..models import Prospectos

def get_all_prospectos():
    return Prospectos.objects.all()

def get_prospectos(prospectos_pk):
    return Prospectos.objects.get(pk=prospectos_pk)