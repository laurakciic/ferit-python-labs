from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    txt = 'Radi'
    return HttpResponse(txt)

def about(request):
    txt = "Laura"
    return HttpResponse(txt)