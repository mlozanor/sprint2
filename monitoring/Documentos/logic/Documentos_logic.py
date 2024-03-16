from ..models import Documentos

def get_all_documentos():
    return Documentos.objects.all()

def get_documentos(documentos_pk):
    return Documentos.objects.get(pk=documentos_pk)