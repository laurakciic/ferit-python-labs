from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from .models import Image, Comment

# Create your views here.
def index(request):
    # txt = 'Radi'
    # return HttpResponse(txt)
    images = Image.objects.order_by('-pub_date')
    context = {
        'all_images': images, 
    }
    return render(request, 'images/index.html', context)

def detail(request, image_id):
    image = get_object_or_404(Image, pk = image_id)
    context = {
        'image': image, 
    }
    return render(request, 'images/detail.html', context)

def about(request):
    # txt = "Laura"
    # return HttpResponse(txt)
    context = {}
    return render(request, 'images/about.html', context)