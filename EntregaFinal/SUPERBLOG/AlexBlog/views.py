from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AlexBlog.models import Entrada
# Create your views here.
def home(request):
    articulos = Entrada.objects.all()
    return render(request, "index.html", {"articulos": articulos})

def registro(request):
    if request.method == 'GET':
        return render(request, "registro.html", { 'form': UserCreationForm } )
    else:
        if request.POST['password1']!= request.POST['password2']:
            return render(request, "registro.html" , { 'form': UserCreationForm , 'data': "Password no coincidente!"})
        else:
            name = request.POST["username"]
            password = request.POST["password1"]
            user = User.objects.create_user(username = name , password = password)
            user.save()
            return render(request, "registro.html" , { 'form': UserCreationForm , 'data': "Usuario creado!"})
    return render(request, "registro.html", { 'form': UserCreationForm })

def login(request):
    return render(request, "login.html")

