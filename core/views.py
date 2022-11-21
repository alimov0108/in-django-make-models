from django.shortcuts import render
from .models import Post

def index(request):
    malumotlar = Post.objects.all()
    qolip = {
        'malumotlar': malumotlar
    }

    return render(request, 'index.html', qolip)
