from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def welcome(request):
    return HttpResponse("<h1>Welcome!</h1>")

def kovacic(request):
    return HttpResponse("<h1>kovacic</h1>")