from django.urls import path
from . import views

app_name = 'form'
urlpatterns = [
    path('', views.index, name='index'),
    path('recent/', views.recent, name='recent'),
    path('post/', views.recent, name='post'),
    path('edit/<int:id>', views.edit, name='edit'),
    # path('edit/<int:id>', views.updaterecord, name='updaterecord'),
    path('delete/<int:id>', views.delete, name='delete'),
]