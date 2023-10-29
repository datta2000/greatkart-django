from django.shortcuts import render
from store.models import product

def home(request):
    products = product.objects.all().filter(is_available=True)

    context = {
        'products':products,

    }
    return render(request, 'home.html',context)