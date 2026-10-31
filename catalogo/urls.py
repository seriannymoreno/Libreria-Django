
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('libros/', views.listar_libros, name='listar_libros'),
]