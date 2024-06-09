
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields=['name', 'quantity', 'category']
        widgets= {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }