from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def creating(request):
    return render(request, 'new_post.html')