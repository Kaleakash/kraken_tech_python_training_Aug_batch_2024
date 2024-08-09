
from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path("add_product",views.add_product),
    path("add_product_info",views.add_product_info),
    path("delete_product",views.delete_product),
    path("update_product",views.update_product),
    path("view_product",views.view_product),
]