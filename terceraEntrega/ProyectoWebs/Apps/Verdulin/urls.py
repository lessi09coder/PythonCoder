from django.contrib import admin
from django.urls import path
from .views import index, login, add_producto, buscar_producto

urlpatterns = [        
    path('index/', index),
    path('login/', login),
    path('productos/', buscar_producto),
    path('agregarProductos/', add_producto),
    path('buscarProductos/', buscar_producto),
]