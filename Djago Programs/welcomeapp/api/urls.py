
from django.urls import path
from . import views

urlpatterns=[
    path("employees/",views.employee_api),
    path("departments/",views.department_api),
    
]