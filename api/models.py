from django.db import models

class Sehir(models.Model):
    sehir_adi = models.CharField(max_length=100)

    def __str__(self):
        return self.sehir_adi

    class Meta:
        verbose_name_plural = "Sehirler"

class Ilce(models.Model):
    sehir = models.ForeignKey(Sehir,on_delete=models.CASCADE)
    ilce_adi = models.CharField(max_length=100)
    ilce_id = models.IntegerField()

    def __str__(self):
        return self.ilce_adi

    class Meta:
        verbose_name_plural = "İlçeler"