from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('recent/', views.recent, name='recent'),
    path('post/', views.recent, name='post'),
    path('', views.index, name='index')
]