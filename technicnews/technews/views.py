from django.shortcuts import render
from .models import Post


def index(request):
    return render(request, 'index.html')

def creating(request):
    return render(request, 'new_post.html')

def check_posts(request):
    posts = Post.objects.all()
    return render(request, 'check_post.html', {'posts': posts})