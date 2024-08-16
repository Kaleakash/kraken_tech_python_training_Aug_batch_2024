from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def view_product(request):

    return render(request,"view_product.html")
