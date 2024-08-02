from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("Welcome to Django First App module")
    return HttpResponse(''' 
            <div>
                  <h2>Welcome to First_App sub module</h2>
                <a href="about_us">AboutUs</a>|
                <a href="contact_us">ContactUs</a>|
                <a href="feedback">Feedback</a>|      
            </div>
    ''')

def about_us(request):
    return HttpResponse("Welcome to Django First App module About Us ")

def contact_us(request):
    return HttpResponse("Welcome to Django First App module Contact us")

def feedback(request):
    return HttpResponse("Welcome to Django First App module Feedback")
