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


def add_product(request):
    return render(request,"add_product.html")

def add_product_info(request):
    pname=request.POST.get("pname")
    price = request.POST.get("price")

    p1=Product(product_name=pname,product_price=price)
    p1.save()

    context = {"result":"Product details stored successfully"}
    return render(request,"add_product.html",context)

def delete_product(request):
    return render(request,"delete_product.html")

def delete_product_info(request):
    pid = request.GET.get("pid")

    result = Product.objects.filter(id=pid).delete()
    print(result)
    if result.__contains__(0):
        context = {"result":"Record not present"}
    else:
        context={"result":"Record deleted successfully"}
    return render(request,"delete_product.html",context)









