from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def index(request):
    return render(request, 'index.html')

def creating(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма неверно заполнена'

    form = PostForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'new_post.html')

def check_posts(request):
    posts = Post.objects.all()
    return render(request, 'check_post.html', {'posts': posts})