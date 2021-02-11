# coding: utf-8
from django.core.management.base import BaseCommand, CommandError
import requests
import bs4
import re
from api.models import Sehir,Ilce
import sys

class Command(BaseCommand):
    def get_sehirler(self):
        link = "https://namazvakitleri.diyanet.gov.tr/tr-TR/{}"
        now = 9146
        stop = 9956
        sehirler = {}
        FORMAT = "var srSehirAdi = \"(.+)\";"
        sayac = 0

        while now < stop:
            s = requests.get(link.format(now))
            parser = bs4.BeautifulSoup(s.content,"html.parser")
            sehir = re.search(FORMAT,s.content.decode("utf-8"))
            if(sehir):
                sehir = sehir.group(1)
                sys.stdout.write("\r{} için bilgiler alınıyor {:<10}".format(sehir,""))
                sys.stdout.flush()
                sayac += 1
            else:
                exit(0)
            ilceler = [i for i in parser.find("select",{"class":"district-select"}).findAll("option")]
            while True:
                x = int(ilceler[-1].get("value"))
                if(x-now>50):
                    ilceler = ilceler[:len(ilceler)-1]
                    continue
                else:
                    now = x+1
                    break
            sehirler[sehir] = {i.text:i.get("value") for i in ilceler}

        print("\nToplam",sayac,"şehir")
        return sehirler

    def handle(self,*args,**options):
        # Sehirleri kaydetme
        sehirler = self.get_sehirler()
        Sehir.objects.all().delete()
        Ilce.objects.all().delete()

        for i in sehirler:
            x = Sehir()
            x.sehir_adi = i.lower()
            x.save()

        for index,i in enumerate(sehirler):
            sehir = Sehir.objects.get(sehir_adi=i.lower())
            ilceler = sehirler[i]

            for k in ilceler:
                ilce = Ilce()
                ilce.sehir = sehir
                ilce.ilce_adi = "merkez" if sehir.sehir_adi == k.lower() else k.lower()
                ilce.ilce_id = ilceler[k]
                ilce.save()
                sys.stdout.write("\r({:>2}) {} ili {} ilçesi kaydedildi{:<20}".format(index+1,sehir.sehir_adi,k,""))
                sys.stdout.flush()

        print("\nTüm işlemler tamam!")