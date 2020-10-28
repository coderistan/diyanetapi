# coding: utf-8

from api.views import sehirler,ilceler,vakitler
from django.urls import path

urlpatterns = [
    path("sehirler/",sehirler),
    path("ilceler/<int:sehir_id>",ilceler),
    path("vakitler/<int:ilce_id>",vakitler)
]