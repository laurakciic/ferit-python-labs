from typing import Text
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Image, Comment, Vote, Like
from .forms import CommentForm, ImageForm
import random

# Create your views here.

def index(request):
    images = Image.objects.order_by('-pub_date')
    votes = [ image.vote_by(request.user) for image in images ]
    context = { 'images_with_votes': zip(images, votes) }
    return render(request, 'app/index.html', context)

def detail(request, image_id):
    image = get_object_or_404(Image,pk=image_id)
    if request.user.is_superuser:
        context = {'image': image, 
                    'vote': image.vote_by(request.user),
                    'comments': image.comment_set.all(),
                    'form': CommentForm(),
                }
    else:
        context = {'image': image, 
                    'vote': image.vote_by(request.user),
                    'comments': image.comment_set.filter(approved=True),
                    'form': CommentForm(),
                }
    return render(request, 'app/detail.html', context)

def create_image(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = ImageForm(request.POST)
        if form.is_valid():
            saved_image = form.save(commit=False)
            saved_image.user = request.user
            saved_image.save()
            return HttpResponseRedirect(reverse('app:detail', args=(saved_image.id,)))
    else:
        form = ImageForm()
    context = { 'form':form, 'action':'create'}
    return render(request, 'app/create_image.html', context)

def delete_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    if request.method=='POST' and (image.user == request.user or request.user.is_superuser):
        image.delete()
    return HttpResponseRedirect(reverse('app:index'))

def update_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    if request.method == 'POST' and (image.user == request.user or request.user.is_superuser):
        form = ImageForm(request.POST, instance = image)
        if form.is_valid():
            saved_image = form.save()
            return HttpResponseRedirect(reverse('app:detail', args=(saved_image.id,)))
    else:
        form = ImageForm(instance=image)
    context = { 'form':form, 'action':'update'}
    return render(request, 'app/create_image.html', context)


def comment(request, image_id):
    if request.method == 'POST' and request.user.is_authenticated:
        image = get_object_or_404(Image, pk=image_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.image = image
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(reverse('app:detail',
            args=(comment.image.id,)))
        else:
            return render(request, 'app/detail.html', {
                'image': image,
                'comments' : image.comment_set.all(),
                'form': form,
            })
    else:
        return HttpResponseRedirect(reverse('app:detail', args=(
            image_id,
        )))
def approve(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST' and request.user.is_superuser:         
        comment.approve()
    return HttpResponseRedirect(reverse('app:detail', args=(comment.image.id,)))

def vote(request, image_id, upvote):
    image = get_object_or_404(Image, pk=image_id)
    vote= Vote.objects.filter(user=request.user, image=image).first()
    if vote:
        if vote.upvote == upvote:
            vote.delete()
            return None
        else:
            vote.upvote = upvote
    else:
        vote= Vote(user=request.user, image=image, upvote=upvote)
        try:
            vote.full_clean()
            vote.save()
        except:
            return None
        else:
            return vote

def upvote(request, image_id):
    if request.method == 'POST' and request.user.is_authenticated:
        vote(request, image_id, True)
    return HttpResponseRedirect(reverse('app:detail', args=(image_id,)))

def downvote(request, image_id):
    if request.method == 'POST' and request.user.is_authenticated:
        vote(request, image_id, False)
    return HttpResponseRedirect(reverse('app:detail', args=(image_id,)))

def like(request, comment_id, likestatus):
    comment = get_object_or_404(Comment, pk=comment_id)
    likecomm= Like.objects.filter(user=request.user, comment=comment).first()
    if likecomm:
        if likecomm.likecomment == likestatus:
            likecomm.delete()
            return None
        else:
            likecomm.likecomment=likestatus
    else:
        likecomm = Like(user=request.user, comment=comment, likecomment = likestatus)
        try:
            likecomm.full_clean()
            likecomm.save()
        except Exception as e:
            print(e)
            return None
        else:
            return likecomm

def likebtn(request, comment_id, image_id):
    if request.method == 'POST' and request.user.is_authenticated:
        like(request, comment_id, True)
    return HttpResponseRedirect(reverse('app:detail', args=(image_id,)))
