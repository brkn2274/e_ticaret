from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Ürün
from .forms import ÜrünForm

# Signup fonksiyonu
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Login sayfasına yönlendirme
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Ürünlerin listelendiği fonksiyon
def urun_list(request):
    urunler = Ürün.objects.all()
    return render(request, 'urun_list.html', {'urunler': urunler})

# Yeni ürün oluşturma fonksiyonu
def urun_create(request):
    if request.method == 'POST':
        form = ÜrünForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('urun_list')
    else:
        form = ÜrünForm()
    return render(request, 'urun_form.html', {'form': form})

# Ürün silme fonksiyonu
def urun_delete(request, id):
    urun = get_object_or_404(Ürün, id=id)
    if request.method == 'POST':
        urun.delete()
        return redirect('urun_list')
    return render(request, 'urun_confirm_delete.html', {'urun': urun})
def home(request):
    return render(request, 'home.html')