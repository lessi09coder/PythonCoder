from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from AlexBlog.models import Entrada, Usuario
from AlexBlog.forms import FormularioRegistroUsuario, LoginUsuarios
from django.contrib.auth import authenticate, login, logout


# Create your views here.


# @login_required
def home(request):
    articulos = Entrada.objects.all()
    return render(request, "index.html", {"articulos": articulos})


def registro(request):
    if request.method == "POST":
        existeUser = Usuario(username=request.POST['username'])
        existe = existeUser.siExiste()
        if existe:
            return render(
                request, "index.html", {"data": f"ya existe el usuario {existeUser}"}
            )
        form = FormularioRegistroUsuario(request.POST)
        print(f"is valid?: {form.is_valid()}")

        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            password = form.cleaned_data["password1"]

            obj = Usuario(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
            )

            obj.save()
            return render(
                request,
                "index.html",
                {"data": f"Se dio de alta el usuario {obj}"},
            )
    else:
        form = FormularioRegistroUsuario()

        return render(request, "registro.html", {"form": form})


""" def login(request):
    return HttpResponse("hola")
 """


def loginUser(request):
    if request.method == "POST":
        form = LoginUsuarios(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            print(cd["password1"])
            user = authenticate(
                request, username=cd["username"], password=cd["password1"]
            )

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("usuario autenticado")
                else:
                    return HttpResponse("usuario no activo")

            else:
                return HttpResponse("usuario es un NONE")

    else:
        form = LoginUsuarios()
        return render(request, "login.html", {"form": form})


def logoutUser(request):
    logout(request)
    return redirect("login")
