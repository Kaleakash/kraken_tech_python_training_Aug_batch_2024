from django.shortcuts import render
from django.http import HttpResponse

course=[
    {"cid":100,"cname":"Java"},
    {"cid":101,"cname":"Python"},
    {"cid":102,"cname":"Node JS"},
    {"cid":103,"cname":"Angular"},
    {"cid":104,"cname":"React JS"},
    {"cid":105,"cname":"Django"},
]
# Create your views here.
def index(request):
    return HttpResponse("Welcome to course app module")

def course_by_cid(request,cid):
    #return HttpResponse(f'You pass cid as {cid}')
    for c in course:
        if c['cid']==cid:
            return HttpResponse(c.get("cname"))
    return HttpResponse(f'no course present {cid}')

def course_by_cname(request,cname):
    return HttpResponse(f'You pass cname as {cname}')

def course_by_slug(request,info):
    return HttpResponse(f'{info}')


def course_info(request):
    context = {"name":"Akash",
               "desg":"Trainer",
               "tech":["Java","Python","Angular","React JS","Cloud Tech"]
               }
    return render(request,"course_info.html",context)








