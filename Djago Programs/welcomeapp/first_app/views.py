from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Welcome to Django First App module")

def about_us(request):
    return HttpResponse("Welcome to Django First App module About Us ")

def contact_us(request):
    return HttpResponse("Welcome to Django First App module Contact us")

def feedback(request):
    return HttpResponse("Welcome to Django First App module Feedback")
