from django.shortcuts import render, get_object_or_404
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

