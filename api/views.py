from django.views.decorators.cache import cache_page
from rest_framework.views import Response
from rest_framework.decorators import api_view
from api.serializers import SehirSerializer,IlceSerializer,VakitSerializer
from api import models
from api import utils
from diyanetapi.settings import CACHES

timeout = CACHES.get("default").get("TIMEOUT")

@api_view(["GET"])
def sehirler(request):
    veriler = models.Sehir.objects.all()
    veriler = SehirSerializer(veriler,many=True)
    return Response(veriler.data)

@api_view(["GET"])
def ilceler(request,sehir_id):
    sehir = models.Sehir.objects.get(pk=sehir_id)
    ilceler = sehir.ilce_set.all()
    ilceler = IlceSerializer(ilceler,many=True)
    return Response(ilceler.data)

@cache_page(timeout)
@api_view(["GET"])
def vakitler(request,ilce_id):
    veriler = utils.get_times_with_id(ilce_id)
    veriler = VakitSerializer(veriler,many=True)
    return Response(veriler.data)