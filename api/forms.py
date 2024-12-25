from django import forms
from .models import Ürün, Kategori, Müşteri, Sipariş

class ÜrünForm(forms.ModelForm):
    class Meta:
        model = Ürün
        fields = '__all__'

class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = '__all__'

class MüşteriForm(forms.ModelForm):
    class Meta:
        model = Müşteri
        fields = '__all__'

class SiparişForm(forms.ModelForm):
    class Meta:
        model = Sipariş
        fields = '__all__'
