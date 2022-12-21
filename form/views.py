from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse
from .models import Post
from . import forms

def index(request):
    if request.method == 'POST':
        if request.POST.get('nama') and request.POST.get('alamat') and request.POST.get('tgl_lahir') and request.POST.get('email'):
            post = Post()
            post.nama = request.POST.get('nama')
            post.alamat = request.POST.get('alamat')
            post.tgl_lahir = request.POST.get('tgl_lahir')
            post.email = request.POST.get('email')
            post.save()

            return render(request, 'form/index.html')
    else:
        return render(request, 'form/index.html')

def recent(request):
    return HttpResponse("RECENT FORM")
