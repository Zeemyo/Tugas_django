from audioop import reverse
from multiprocessing import context
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404

from django.http import HttpResponse
from django.template import loader
from .models import Post


def index(request):
    db = Post.objects.all()
    context = {
        'post': db,
    }
    if request.method == 'POST':
        if request.POST.get('nama') and request.POST.get('alamat') and request.POST.get('tgl_lahir') and request.POST.get('email'):
            post = Post()
            post.nama = request.POST.get('nama')
            post.alamat = request.POST.get('alamat')
            post.tgl_lahir = request.POST.get('tgl_lahir')
            post.email = request.POST.get('email')
            post.save()

            return render(request, 'form/base.html', context)
    else:
        return render(request, 'form/index.html')

def recent(request):
    return HttpResponse("RECENT FORM")

# def update(request, id):
#     updt = Post.objects.get(id=id)
#     form = Post(instance=forms)
#     data = {
#         'nama': updt.nama,
#         'alamat': updt.alamat,
#         'tgl_lahir': updt.tgl_lahir,
#         'email': updt.email,
#     }
#     classform = forms.classform(request.POST or None, initial=data, instance=updt)

#     if request.method == 'POST':
#         form = Post(request.POST, instance=forms)
#         if classform.is_valid():
#             classform.save()
#             return redirect('form/base.html')
    
#     context = {
#         'heading':'Updt',
#         'classform': classform,
#         'form':'form'
#     }
#     return render(request, 'base.html', context)


def edit(request, id):
    form = Post.objects.get(id=id)
    data = {
         'nama': form.nama,
         'alamat': form.alamat,
         'tgl_lahir': form.tgl_lahir,
         'email': form.email,
     }
     
    if request.method == 'POST':
        if request.POST.get('nama') and request.POST.get('alamat') and request.POST.get('tgl_lahir') and request.POST.get('email'):
            post = Post()
            post.nama = request.POST.get('nama')
            post.alamat = request.POST.get('alamat')
            post.tgl_lahir = request.POST.get('tgl_lahir')
            post.email = request.POST.get('email')
            post.save()

 
    return render(request, 'form/update.html', {'form': form})

    # updt = Post.objects.get(id=id)
    # data = {
    #     'nama': updt.nama,
    #     'alamat': updt.alamat,
    #     'tgl_lahir': updt.tgl_lahir,
    #     'email': updt.email
    # }
    
    # classform = forms.classform(request.POST or None, intitial=data, instance=updt)

    # if request.method == 'POST':
    #     if classform.is_valid():
    #         classform.save()
    #         return HttpResponseRedirect('daftar.html')


    # context = {
    #     'heading': 'updt',
    #     'classform': classform
    # }

    # return render(request, 'base.html', context)
    
    # forms = Post.objects.get(id=id)
    # Post.objects.filter(id=id)
    # context = {
    #      'heading':'Updt',
    #      'form':forms
    #  }
    # return render(request, 'form/update.html', context)

# def updaterecord(request, id):
  
#   post = request.objects.get(id=id)
#   post.nama = request.POST.get['nama']
#   post.alamat = request.POST.get['alamat']
#   post.tgl_lahir = request.POST.get['tgl_lahir']
#   post.email = request.POST.get['email']
#   return render(reverse('/form/'))

def delete(request, id):
    db = Post.objects.all()
    context = {
        'post': db,
    }
    Post.objects.filter(id=id).delete()
    return render(request, 'form/base.html', context)