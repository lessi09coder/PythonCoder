from django.shortcuts import render

from AlexBlog.models import Entrada
# Create your views here.
def home(request):
    articulos = Entrada.objects.all()
    return render(request, "index.html", {"articulos": articulos})