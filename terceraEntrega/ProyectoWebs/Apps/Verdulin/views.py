from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from .models import Producto

def index(request):
    return render(request, 'index.html')

def login(request):
    return HttpResponse('hola login 1111')

def ver_producto(request):
    producto1 = Producto(nombre = "manzana", precio = "100.10", cantidad = 7)
    producto1.save()

    return HttpResponse('producto agregado')