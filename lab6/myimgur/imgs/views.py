from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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
        # (query set za kom tog tipa), lista svih komentara te image
    }
    return render(request, 'imgs/detail.html', context)

def comments(request):
    comments = Comment.objects.order_by('nick')
    context = {
        'comments': comments
    }
    return render(request, 'imgs/comments.html', context)

def post_comment(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    comment = image.comment_set.create(
        # plavo je field (nick) modela a narancasto naziv parametra (nick)
        nick = request.POST['nick'],
        text = request.POST['text'],
    )
    # redirecta na root aplikacije
    return HttpResponseRedirect(reverse('detail', args=(image.id,)))

def about(request):
    context = {}
    return render(request, 'imgs/about.html', context)
