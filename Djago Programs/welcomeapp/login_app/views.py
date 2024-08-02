from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"login.html")

def check_login_with_get_method(request):
    print(request.GET)
    emailid = request.GET.get("emailid")
    password = request.GET.get("password")
    if emailid=="akash@gmail.com" and password=="123":
        return render(request,"success.html")
    else:
        return render(request,"failure.html") 
    

def check_login_with_post_method(request):
    print(request.POST)
    emailid = request.POST.get("emailid")
    password = request.POST.get("password")
    if emailid=="akash@gmail.com" and password=="123":
        return render(request,"success.html")
    else:
        return render(request,"failure.html") 
     
