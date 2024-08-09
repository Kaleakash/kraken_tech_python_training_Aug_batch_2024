from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def add_product(request):
    return render(request,"add_product.html")

def delete_product(request):
    return render(request,"delete_product.html")

def update_product(request):
    return render(request,"update_product.html")

def view_product(request):
    return render(request,"view_product.html")


