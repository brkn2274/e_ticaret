"""
URL configuration for e_ticaret project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from django.contrib.auth import views as auth_views
from api import views  # api/views.py içindeki tüm fonksiyonlar kullanılabilir
from api.views import signup, home  # signup fonksiyonunu doğrudan import ediyoruz

urlpatterns = [
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('urunler/', views.urun_list, name='urun_list'),  # views.urun_list
    path('urunler/yeni/', views.urun_create, name='urun_create'),  # views.urun_create
    path('urunler/<int:id>/sil/', views.urun_delete, name='urun_delete'),  # views.urun_delete
    path('signup/', signup, name='signup'),  # Doğrudan signup
]

