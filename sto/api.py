from django.http import JsonResponse
from sto.models import Sto, StoService
from sto.serializers import StoSerializer, ServicesSerializer

def get_stos(request):
    stos = StoSerializer(
    Sto.objects.all().order_by('-id'),
    many=True,
    context={'request': request}
    ).data
    return JsonResponse({'stos':stos})

def get_services(request, sto_id):
    services = ServicesSerializer(
    StoService.objects.all().filter(sto_id=sto_id).order_by('-id'),
    many=True,
    context={'request': request}
    ).data
    return JsonResponse({'services': services})
