from django.contrib import admin
from .models import Kategori, Ürün, Müşteri, Sipariş, SiparişÜrünleri

admin.site.register(Kategori)
admin.site.register(Ürün)
admin.site.register(Müşteri)
admin.site.register(Sipariş)
admin.site.register(SiparişÜrünleri)
