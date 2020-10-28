# coding: utf-8

import requests
import bs4
from api.models import Ilce

class Vakit:
    def __init__(self,bilgiler,index):
        self.index = index
        self.tarih = bilgiler[0].text
        self.imsak = bilgiler[1].text
        self.gunes = bilgiler[2].text
        self.ogle = bilgiler[3].text
        self.ikindi = bilgiler[4].text
        self.aksam = bilgiler[5].text
        self.yatsi = bilgiler[6].text

def get_object_or_none(cls,**pr):
    try:
        return cls.objects.get(**pr)
    except Exception as e:
        return None

# TODO: ID verilen belde hakkında aylık veriler çekilecek
def get_times_with_id(county_id):
    ilce = get_object_or_none(Ilce,ilce_id=county_id)
    if ilce == None:
        return None

    sayfa = requests.get("https://namazvakitleri.diyanet.gov.tr/tr-TR/{}".format(county_id))
    parser = bs4.BeautifulSoup(sayfa.content,"html.parser")

    tab = parser.find("div",{"id":"tab-1"})
    vakitler = tab.find_all("tr")
    vakitler = vakitler[1:]
    result = []
    for index,i in enumerate(vakitler):
        bilgiler = i.find_all("td")
        result.append(Vakit(bilgiler,index+1))
            
    return result 