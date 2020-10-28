# coding: utf-8

from rest_framework import serializers
from api.models import Sehir,Ilce

class SehirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sehir
        fields = ["sehir_adi","id"]
class IlceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ilce
        fields = ["ilce_adi","ilce_id"]
class VakitSerializer(serializers.Serializer):
    index = serializers.IntegerField()
    tarih = serializers.CharField()
    imsak = serializers.CharField()
    gunes = serializers.CharField()
    ogle = serializers.CharField()
    ikindi = serializers.CharField()
    aksam = serializers.CharField()
    yatsi = serializers.CharField()