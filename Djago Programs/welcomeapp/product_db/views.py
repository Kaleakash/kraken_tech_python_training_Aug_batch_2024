from django.shortcuts import render
from .models import Product;

# Create your views here.

def index(request):
    print("index page")
    return render(request,"index.html")

def view_product(request):
    products = Product.objects.values()     # connect with model to get the data.  
    print(products)
    context = {"products":products}
    return render(request,"view_product.html",context)
