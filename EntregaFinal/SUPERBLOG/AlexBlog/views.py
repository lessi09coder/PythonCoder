from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from AlexBlog.models import Entrada
from AlexBlog.forms import FormularioRegistroUsuario, LoginUsuarios, AgregarArticulos
from django.contrib.auth import authenticate, login, logout


# Create your views here.


# @login_required
def home(request):
    articulos = Entrada.objects.all()
    return render(request, "index.html", {"articulos": articulos})
    
def registro(request):
    if request.method == "POST":
        """ existeUser = User(username=request.POST['username'])
        existe = existeUser.siExiste()
        if existe:
            return render(
                request, "index.html", {"data": f"ya existe el usuario {existeUser}"}
            ) """
        form = FormularioRegistroUsuario(request.POST)
        print(f"is valid?: {form.is_valid()}")

        if form.is_valid():
            User.objects.create_user(username=request.POST['username'], first_name = request.POST['first_name'],last_name = request.POST['last_name'], password =request.POST['password1'])
            
            
            """ username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            password = form.cleaned_data["password1"]

            obj = User(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password1=password,
                password2=password
            )

            obj.save() """
            return render(
                request,
                "index.html",
                {"data": f"Se dio de alta el usuario "},
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
            user = authenticate(username=cd["username"], password=cd["password1"])
            print(f" autenticacion del usuario {user}")
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect ("/")
                   # ACOMODAR ESTOD DE ABAJO
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

# @login_required
def agregarArticulos(request):
    # articulos = Entrada.objects.all()
    
    if request.method == "POST":
        form = AgregarArticulos(request.POST)
        print(f" AgregarArticulos is valid?: {form.is_valid()}")
        if form.is_valid():
            titulo = form.cleaned_data["titulo"]
            subtitulo = form.cleaned_data["subtitulo"]
            cuerpo = form.cleaned_data["cuerpo"]
            #imagen = form.cleaned_data["imagen"]
            
            obj = Entrada(
                titulo=titulo,
                subtitulo=subtitulo,
                cuerpo=cuerpo,
               # imagen=imagen,                            
            )
            #mmmm esto sirve?
            
            obj.autor = request.user
            obj.save()
            
            #el autor no encuentra id, corregir en video mostrado por FASTZ
            
            
            # nuevo_articulo.Usuario = request.Usuario
            # nuevo_articulo = form.save(comit=False)
            
            return redirect(registro)
    else:
        form = AgregarArticulos()
        return render(request, "agregarArticulos.html", {"form": form})
    
        
"""     
>>> r = Reporter(first_name="John", last_name="Smith", email="john@example.com")
>>> r.save()

>>> r2 = Reporter(first_name="Paul", last_name="Jones", email="paul@example.com")
>>> r2.save()
Create an Article:

>>> from datetime import date
>>> a = Article(id=None, headline="This is a test", pub_date=date(2005, 7, 27), reporter=r)
>>> a.save()

>>> a.reporter.id
1

>>> a.reporter
<Reporter: John Smith> """

# def borrarProducto(request, id):   