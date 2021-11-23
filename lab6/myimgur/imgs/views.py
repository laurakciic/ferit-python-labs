from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Image, Comment

# Create your views here.
def index(request):
    images = Image.objects.order_by('-pub_date')
    context = {
        'all_images': images
    }
    return render(request, 'imgs/index.html', context)

def detail(request, image_id):
    image = get_object_or_404(Image,pk=image_id)
    context = {
        'image': image,
        'comments': image.comment_set.all()
    }
    return render(request, 'imgs/detail.html', context)

def about(request):
    context = {}
    return render(request, 'imgs/about.html', context)
