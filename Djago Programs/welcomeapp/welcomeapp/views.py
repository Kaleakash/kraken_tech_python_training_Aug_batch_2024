from django.http import HttpResponse


def index(request):
        return HttpResponse("Welcome to My Django App Page")

def about_us(request):
        return HttpResponse("Welcome to About Us page")