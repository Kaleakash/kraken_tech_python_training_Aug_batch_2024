from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path("course_by_cid/<int:cid>",views.course_by_cid),
    path("course_by_cname/<str:cname>",views.course_by_cname),
    path("course_by_slug/<slug:info>",views.course_by_slug)
]