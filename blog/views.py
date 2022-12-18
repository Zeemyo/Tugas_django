from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse
from .models import Post

def index(request):
    db = Post.objects.all()
    context = {
        'Judul' : 'Blog Blog-an',
        'h1' : 'About Me',
        'Nama' : 'Zidan Alamsyah Amir',
        'NPM' : '1204057',
        'Asal' : 'Jakarta Utara, Jakarta',
        'Email' : 'zidanalam96@gmail.com',
        'HP' : '085157113317',
        'Umur' : '21',
        'Desc' : 'Orang',
        'title':'Blog',
        'heading':'Blog',
        'subheading':'postingan',
        'post': db,
    }

    return render(request, 'blog/index.html', context)

def recent(request):
    return HttpResponse("RECENT BLOG")
    #context = {
    #    'Judul' : 'blog2',
    #    'h1' : 'Python'
    #}  
    #return render(request, 'blog/index.html', context)
# Create your views here