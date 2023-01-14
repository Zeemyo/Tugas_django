from django.db import models
from django.utils.text import slugify
# from . import validators
# Create your models here.

class Post(models.Model):
    nama= models.CharField(max_length=100, unique=True)
    alamat= models.TextField()
    tgl_lahir = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    slug = models.SlugField(blank=True, editable=False)

# class Post(models.Model):
#     nama = models.CharField(max_length=25)
#     alamat = models.TextField()
#     tgl_lahir = models.TextField()
#     email = models.EmailField(blank=True)
#     slug = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.nama)
        super(Post, self).save()

    def _str_(self):
        return "{}".format(self.nama)