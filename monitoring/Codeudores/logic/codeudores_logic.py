from ..models import Codeudores

def get_all_codeudores():
    return Codeudores.objects.all()

def get_codeudores(codeudores_pk):
    return Codeudores.objects.get(pk=codeudores_pk)