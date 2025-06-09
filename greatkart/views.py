from django.shortcuts import render 
from store.models import Product

def home(request):
    availableProducts = Product.objects.all().filter(is_available = True)

    context = { 'products' : availableProducts }

    return render(request,'home.html', context)