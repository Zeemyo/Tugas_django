from django.urls import path
from . import views

app_name = 'form'
urlpatterns = [
    path('', views.index, name='index'),
    path('recent/', views.recent, name='recent'),
    path('post/', views.recent, name='post'),
]