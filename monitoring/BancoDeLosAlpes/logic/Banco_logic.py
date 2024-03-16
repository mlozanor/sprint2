from ..models import BancoDeLosAlpes

def get_all_bancos():
    return BancoDeLosAlpes.objects.all()

def get_bancos(banco_pk):
    return BancoDeLosAlpes.objects.get(pk=banco_pk)