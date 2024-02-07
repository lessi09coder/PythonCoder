from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from AlexBlog.models import Entrada
from AlexBlog.forms import FormularioRegistroUsuario, AgregarArticulos


from django.contrib.auth import authenticate, login, logout


# Create your views here.
class Home(TemplateView):
    template_name = "index.html"


# @login_required
""" def home(request):
    articulos = Entrada.objects.all()
    return render(request, "index.html", {"articulos": articulos})
     """


class RegistroUsuarios(CreateView):
    form_class = FormularioRegistroUsuario
    template_name = "registro.html"

    def get_success_url(self):
        return reverse_lazy("home")


class LoginUser(LoginView):
    template_name = "login.html"
    fields = "__all__"
    # redirect_autheticated_user = True
    # success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy("home")


class LogoutUser(LogoutView):
    def get_success_url(self):
        return reverse_lazy("login")


class AgregarArticulos(CreateView, LoginRequiredMixin):    
    form_class = AgregarArticulos
    template_name = "agregarArticulos.html"
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("agregarArticulos")    
        
class VerArticulos(ListView,LoginRequiredMixin):
    model = Entrada
    template_name = 'todosArticulos.html'
    context_object_name = 'articulos'
    ordering = ['-fecha']
    #ordering = ['-date_published']  # Opcional: ordena los artículos por fecha de publicación

class ArticuloDetalle(DetailView):
    model = Entrada
    template_name = 'articuloDetalle.html'
    context_object_name = 'articulo'
#crear la class para ver articulos:  
   


class SobreMi(TemplateView):
    template_name = 'sobreMi.html' 
   
# @login_required
# este se puede borrar
def agregarArticulos(request):
    # articulos = Entrada.objects.all()

    if request.method == "POST":
        form = AgregarArticulos(request.POST)
        print(f" AgregarArticulos is valid?: {form.is_valid()}")
        if form.is_valid():
            titulo = form.cleaned_data["titulo"]
            subtitulo = form.cleaned_data["subtitulo"]
            cuerpo = form.cleaned_data["cuerpo"]
            # imagen = form.cleaned_data["imagen"]

            obj = Entrada(
                titulo=titulo,
                subtitulo=subtitulo,
                cuerpo=cuerpo,
                # imagen=imagen,
            )
            # mmmm esto sirve?

            obj.autor = request.user
            obj.save()

            # el autor no encuentra id, corregir en video mostrado por FASTZ

            # nuevo_articulo.Usuario = request.Usuario
            # nuevo_articulo = form.save(comit=False)

            return redirect(agregarArticulos)
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
