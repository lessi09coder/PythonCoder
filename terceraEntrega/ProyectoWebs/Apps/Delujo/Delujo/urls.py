from django.contrib import admin
from django.urls import path
from .views import index, login

urlpatterns = [        
    path('index/', index),
    path('login/', login),
]