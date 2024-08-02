

from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path("about_us",views.about_us),
    path("contact_us",views.contact_us),
    path("feedback",views.feedback),
]

# http://localhosst:8000/first/