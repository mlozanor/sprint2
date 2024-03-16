from ..models import Documentos

def get_all_documentos():
    return Documentos.objects.all()

def get_documentos(documentos_pk):
    return Documentos.objects.get(pk=documentos_pk)

def create_documentos(documentos):
    return Documentos.objects.create(
        nombre=documentos['nombre'],
        descripcion=documentos['descripcion'],
        fecha_creacion=documentos['fecha_creacion'],
        fecha_modificacion=documentos['fecha_modificacion'],
        usuario_creacion=documentos['usuario_creacion'],
        usuario_modificacion=documentos['usuario_modificacion']
    )