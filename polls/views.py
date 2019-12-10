from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello Django")


def detail(request,id):
    return HttpResponse("You are looking at Question no {0}" .format(id))


def result(request,id):
    return HttpResponse("You are looking at the result of Question no {0}".format(id))

def voting(request,id):
    return HttpResponse("You are voting on Question no {0}".format(id))


