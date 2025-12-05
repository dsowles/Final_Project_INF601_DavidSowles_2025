
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'detail.html', {'post': post})

@login_required
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blog-detail", slug=post.slug)
    else:
        form = PostForm()

    return render(request, "create.html", {"form": form})

@login_required
def delete(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        post.delete()
        return redirect("home")

    return render(request, "delete.html", {"post": post})

@login_required
def update(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-detail', slug=post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, 'update.html', {'form': form, 'post': post})

def search(request):
    return HttpResponse('Search Blog Page')



@login_required
def account_dashboard(request):
    # Show only posts the logged-in user created (recommended)
    posts = Post.objects.filter(author=request.user).order_by('-created_at')

    return render(request, "account/dashboard.html", {
        "posts": posts,
})

def about(request):
    return render(request, 'about.html')