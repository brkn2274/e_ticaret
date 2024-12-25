from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Sipariş, SiparişÜrünleri, Ürün

@receiver(post_save, sender=SiparişÜrünleri)
def update_stock(sender, instance, **kwargs):
    ürün = instance.ürün  # Sipariş edilen ürün
    miktar = instance.miktar  # Sipariş miktarı
    ürün.stok_miktarı -= miktar
    ürün.save()
