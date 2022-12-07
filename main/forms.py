from django import forms
from .models import Sinf, Dars


class SinfForm(forms.ModelForm):
    class Meta:
        model = Sinf
        fields = ('name_uz', 'name_ru')


class DarsForm(forms.ModelForm):
    class Meta:
        model = Dars
        fields = ('sinf', 'fan_nomi_uz', 'fan_nomi_ru', 'hafta_kuni', 'soat')