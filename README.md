"# E-Ticaret Projesi" 
# E-Ticaret Yönetim Paneli Projesi

Bu proje, Ankara Üniversitesi Yapay Zeka ve Veri Mühendisliği YZM311 Veri Tabanı Yönetim Sistemleri dersi için geliştirilmiş bir e-ticaret yönetim panelidir. Django framework kullanılarak hazırlanmıştır ve MySQL veritabanı ile entegre edilmiştir.

---

## **Proje Bilgileri**
- **Öğrenci Adı/Soyadı:** Barkın Yılmaz
- **Öğrenci No:** 123456789
- **Ders Kodu:** YZM311 Veri Tabanı Yönetim Sistemleri

---

## **Proje Özellikleri**
- **Kullanıcı İşlemleri:**
  - Kullanıcı kayıt olma ve giriş yapma (Signup/Login).
  - Çıkış yapma (Logout).
- **CRUD İşlemleri:**
  - Ürün ekleme, listeleme, güncelleme ve silme.
  - Kategorilere göre ürün yönetimi.
- **Sipariş Yönetimi:**
  - Sipariş ekleme, listeleme ve ilişkili stok yönetimi.
- **Veritabanı İşlemleri:**
  - MySQL tetikleyicileri (Trigger) kullanılarak stok yönetimi sağlandı.

---

## **Kurulum ve Çalıştırma**

### 1. **Projeyi Klonlayın**
Aşağıdaki komutla projeyi bilgisayarınıza indirin:
```bash
git clone https://github.com/brkn2274/e_ticaret.git
cd e_ticaret
Proje Özeti: Django framework’ü kullanarak bir e-ticaret yönetim paneli geliştirme üzerine kuruldu

Kullanıcıların kayıt olabildiği, giriş yapabildiği ve ürün/sipariş yönetimi yapabildiği bir sistem oluşturdum. Bu süreçte MySQL veri tabanı entegrasyonu sağlandı ve gerekli tüm CRUD (Create, Read, Update, Delete) işlemleri uygulandı.

Adım Adım Neler Yapıldı?

Django Projesi Başlatıldı

Django framework’ü kullanarak bir proje oluşturuldu.

django-admin startproject e_ticaret

Proje için gerekli uygulama (api) oluşturudu:
python manage.py startapp api

MySQL Veri tabanı Entegrasyonu yapıldı
MySQL ile Django arasında bağlantı kuruldu.

settings.py dosyasında gerekli veri tabanı ayarları yapılandırıldı.

DATABASES = {

‘default’: {

‘ENGINE’ : ‘django.db.backends.mysql’,

‘NAME’ : ‘e_ticarert’,

USER

PASSWORD

HOST

PORT

}

}

MySQL üzerinde veri tabanı tabloları oluşturuldu:

kategoriler
ürünler
müşteriler
siparişler
sipariş_ürünleri
Modeller (Models) Tasarlandı
Django modelleri oluşturularak yukarıdaki tabloların Python koduyla eşleştirilmesi sağlandı.
Modeller Üzerinde makemigrations ve migrate komutları çalıştırılarak tablolar MySQL veri tabanına aktarıldı.
Admin Paneli Yapılandırıldı
Admin paneline erişim sağlandı ve admin kullanıcı oluşturuldu: pyhton manage.py createsuperuser
Modeller admin Paneline kaydedildi
Kullanıcı Giriş ve Kayıt İşlemleri (Login/Signup)
Kullanıcıların kayıt ve giriş işlemleri için:
Django’nun yerleşik UserCreationForm ve LoginView sınıfları kullanıldı.
login.html
signup.html oluşturuldu.
6.CRUD İşlemleri (Ürün ve Kategori Yönetimi)

Ürünler ve kategoriler üzerinde ekleme, listeleme, güncelleme ve silme işlemleri için:
Görünümler (views) oluşturuldu
URL’ler yazıldı.
Şablon dosyaları (templates) oluşturuldu
Sipariş Yönetimi ve Trigger Kullanımı
Siparişler oluşturulup listelendi.
Stok miktarı siparişler ile güncellenmek için bir MySQL Trigger yazıldı.
8.Proje Test Edildi

Django geliştirme sunucusu çalıştırıldı:
python manage.py runserver
Projenin tüm sayfaları ve özellikleri test edildi:
Kullanıcı giriş ve kayıt
Admin Paneline erişim
Ürün Ekleme listeleme, silme ve güncelleme
Sipariş oluşturma ve stok yönetimi

