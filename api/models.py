from django.db import models

class Kategori(models.Model):
    kategori_adı = models.CharField(max_length=255)

    def __str__(self):
        return self.kategori_adı

class Ürün(models.Model):
    ürün_adı = models.CharField(max_length=255)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)

    def __str__(self):
        return self.ürün_adı

class Müşteri(models.Model):
    ad = models.CharField(max_length=255)
    soyad = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    şifre = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ad} {self.soyad}"

class Sipariş(models.Model):
    müşteri = models.ForeignKey(Müşteri, on_delete=models.CASCADE)
    sipariş_tarihi = models.DateField()

    def __str__(self):
        return f"Sipariş {self.id} - {self.müşteri.ad}"

class SiparişÜrünleri(models.Model):
    sipariş = models.ForeignKey(Sipariş, on_delete=models.CASCADE)
    ürün = models.ForeignKey(Ürün, on_delete=models.CASCADE)
    miktar = models.IntegerField()

    def __str__(self):
        return f"{self.sipariş} - {self.ürün} x {self.miktar}"
