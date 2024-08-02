from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path("checkLoginWithGet/",views.check_login_with_get_method)
]