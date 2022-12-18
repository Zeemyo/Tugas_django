from django.http import HttpResponse
from django.shortcuts import render
from multiprocessing import context

def index(request):
    context = {
        'judul' : 'Home',
        'h2' : 'This is Home',
        'p' : 'Click the Button Below To See About Me!'
    }
    return render(request, 'index.html', context)

def about(request):
    return render("Ini About")