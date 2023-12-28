from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from .forms import FormularioProducto

#from .models import Producto

def index(request):
    return render(request, 'index.html')


def login(request):
    return HttpResponse('hola login 1111')


def ver_producto(request):    

    return HttpResponse('VER UN PRODUCTO')
    

def add_producto(request):
    if request.method == 'POST':

        form = FormularioProducto(request.POST)
        #print(form)
        if form.is_valid():
            form.save()  
        return render(request, 'index.html')

    else:
         form = FormularioProducto()            

    return render(request, 'formProductos.html', {'form': form})