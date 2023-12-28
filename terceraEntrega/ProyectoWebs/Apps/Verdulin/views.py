from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from .forms import FormularioProducto, FormularioBuscarProducto
from .models import Producto

#from .models import Producto

def index(request):
    return render(request, 'index.html')


def login(request):
    return HttpResponse('hola login 1111')


def buscar_producto(request):    
    if request.method == 'POST':
        form = FormularioBuscarProducto(request.POST)
        if form.is_valid():
            nombre_producto = form.cleaned_data['nombre_producto']
            productos_encontrados = Producto.objects.filter(nombre__icontains = nombre_producto)
            return render(request, 'resultadosBusqueda.html', {'productos': productos_encontrados})
    else:
        form = FormularioBuscarProducto()        

    return render(request, 'formBuscarProductos.html', {'form': form})


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