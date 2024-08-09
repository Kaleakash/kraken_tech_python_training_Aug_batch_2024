from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
path("course_by_cid/<int:cid>",views.course_by_cid)
]