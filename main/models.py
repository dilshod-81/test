from django.db import models
from django.utils.translation import get_language


class Sinf(models.Model):
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50)

    @property
    def name(self):
        return getattr(self, f'name_{get_language()}')

    def __str__(self):
        return self.name


class Dars(models.Model):
    sinf = models.ForeignKey(Sinf, on_delete=models.RESTRICT)
    fan_nomi_uz = models.CharField(max_length=50)
    fan_nomi_ru = models.CharField(max_length=50)
    hafta_kuni = models.SmallIntegerField(choices=(
        (1, "Dushanba"),
        (2, "Seshanba"),
        (3, "Chorshanba"),
        (4, "Payshanba"),
        (5, "Juma"),
        (6, "Shanba"),
        (7, "Yakshanba"),
    ))
    soat = models.TimeField()

    @property
    def fan_nomi(self):
        return getattr(self, f'fan_nomi_{get_language()}')

    def __str__(self):
        return self.fan_nomi
