
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'detail.html', {'post': post})

def create(request):
    return HttpResponse('Create Blog Page')

def delete(request):
    return HttpResponse('Delete Blog Page')

def update(request):
    return HttpResponse('Update Blog Page')

def search(request):
    return HttpResponse('Search Blog Page')
