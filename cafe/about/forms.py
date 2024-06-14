from django.core.exceptions import ValidationError
from django import forms
from .models import Provider
import re


class ProviderForm(forms.Form):
    name = forms.CharField(min_length=10, max_length=255, label='Название компании')
    name_provider = forms.CharField(min_length=2, max_length=50, label='Имя')
    lastname_provider = forms.CharField(min_length=2, max_length=50, label='Фамилия')
    surname_provider = forms.CharField(min_length=2, max_length=50, label='Очество')
    phone = forms.CharField(max_length=20, label='Телефон')
    adress = forms.CharField(min_length=10, label='Адрес')
    
    name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Название компании'})
    name_provider.widget.attrs.update({'class': 'form-control', 'placeholder': 'Имя'})
    lastname_provider.widget.attrs.update({'class': 'form-control', 'placeholder': 'Фамилия'})
    surname_provider.widget.attrs.update({'class': 'form-control', 'placeholder': 'Очество'})
    phone.widget.attrs.update({'class': 'form-control', 'placeholder': 'Телефон'})
    adress.widget.attrs.update({'class': 'form-control', 'placeholder': 'Адрес'})
    
    def clean_telephone(self):
        phone = self.cleaned_data['phone']
        if re.match(r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}', phone):
            return phone
        return False