# Diyanetapi
Diyanet İşleri Başkanlığı sitesinden tüm şehirler için 1 aylık namaz vakitleri sunan Django API

# İlklendirme

Proje Python3 ile çalışır. İlk olarak aşağıdaki komutları girmeniz gerekmektedir.

```
python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py makemigrations api
python manage.py migrate
python manage.py createcachetable
python manage.py ilce_kaydet
```

# Kullanım

Server'ı başlatmak için `python manage.py runserver` komutu girilir.

Sehirlerin listesi: `/api/sehirler`<br/>
Bir sehre ait ilcelerin listesi: `/api/ilceler/sehir_id`<br/>
Bir ilceye ait 1 aylık namaz vakitlerinin listesi: `/api/vakitler/ilce_id`<br/><br/>

Bir şehrin merkezi de ilçe olarak ele alınmıştır. Örneğin Adana'nın merkez ilçesinin namaz vakitleri `/api/vakitler/9146` ile elde edilebilir. 

# Cache sistemi

Projede django cache kullanılmıştır. Bir ilçenin vakitleri elde edildikten sonra o sorgunun sonuçları 1 saatliğine belleğe alınır. Varsayılan olarak 1 saat seçtim, siz isterseniz 1 aylık zaman dilimini saniye olarak hesaplayarak sonuçların 1 ay cache olarak saklanmasını isteyebilirsiniz.

Not: Ticari amaçlı kullanılamaz.
