from placas.models import Placa

def lista_placas(request):
    return{
        "placas": Placa.objects .all()
    }