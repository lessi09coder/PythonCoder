from django.contrib import admin
from django.urls import path
from .views import index, login, ver_producto, add_producto

urlpatterns = [        
    path('index/', index),
    path('login/', login),
    path('productos/', ver_producto),
    path('agregarProductos/', add_producto)
]