from django.shortcuts import render

# Create your views here.

list_of_products=[];

def index(request):
    return render(request,"index.html")

def add_product(request):
    return render(request,"add_product.html")

def add_product_info(request):
    pid = int(request.GET.get("pid"))
    pname = request.GET.get("pname");
    price = float(request.GET.get("price"))

    product = {"pid":pid,"pname":pname,"price":price}

    
    print(product);

    global flag
    flag=0
    for p in list_of_products:
        if p.get("pid")==pid:
            flag=1;
    
    if flag==0:
        list_of_products.append(product);
        context={"result":"Product details added successfully"} 
    else:
        context={"result":"Product id must be unique"} 
    
    return render(request,"add_product.html",context)

def delete_product(request):
    return render(request,"delete_product.html")

def delete_product_info(request):
    pid = int(request.GET.get("pid"))

    global flag
    flag=0
    for p in list_of_products:
        if p.get("pid")==pid:
            list_of_products.remove(p)
            flag=1;
    
    if flag==0:
        context={"result":"Product id not present"} 
    else:
        flag=0;
        context={"result":"Product deleted successfully"} 
    
    return render(request,"delete_product.html",context)

def update_product(request):
    return render(request,"update_product.html")

def view_product(request):
    context={"products":list_of_products}
    return render(request,"view_product.html",context)







