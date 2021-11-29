from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Image, Comment

# Create your views here.

def index(request):
    images = Image.objects.order_by('-pub_date')
    context = { 'images': images}
    return render(request, 'app/index.html', context)

def detail(request, image_id):
    image = get_object_or_404(Image,pk=image_id)
    context = {'image': image, 
               'comments': image.comment_set.all(),
              }
    return render(request, 'app/detail.html', context)

def about(request):
    context = {}
    return render(request, 'app/about.html', context)

def create_image(request):
    try:
        image = Image(
            url = request.POST['image_url'],
            title = request.POST['image_title'],
            pub_date =request.POST['pub_date']    
        )
        image.save()
    except (KeyError, Comment.DoesNotExist):
        # Redisplay the comment posting form.
        return render(request, 'app/new.html', {
            'error_message': "Posting failed!",
        })
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('app:detail', args=(image.id,))) 

def comment(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    try:
        comment = image.comment_set.create(
                   author=request.POST['author'],
                   text=request.POST['comment'],
                )
    except (KeyError, Comment.DoesNotExist):
        # Redisplay the comment posting form.
        return render(request, 'app/detail.html', {
            'image': image,
            'error_message': "Posting failed!",
        })
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('app:detail', args=(image.id,)))

def upvote(request, image_id):
    image = get_object_or_404(Image,pk=image_id)
    if request.method == "POST":
        image.upvotes += 1
        image.save()
    return HttpResponseRedirect(reverse('app:detail', args=(image.id,)))

def downvote(request, image_id):
    image = get_object_or_404(Image,pk=image_id)
    if request.method == "POST":
        image.downvotes += 1
        image.save()
    return HttpResponseRedirect(reverse('app:detail', args=(image.id,)))
