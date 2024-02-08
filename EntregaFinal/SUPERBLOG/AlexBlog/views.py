from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from AlexBlog.models import Entrada
from AlexBlog.forms import FormularioRegistroUsuario, AgregarArticulos, FormularioEdicionUsuario, FormularioEdicionArticulo


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

class EditarUsuario(LoginRequiredMixin,UpdateView):
    form_class = FormularioEdicionUsuario
    template_name= 'editarUsuario.html'
    
    def get_object(self):
        return self.request.user
    
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

class ArticuloDetalle(DetailView):
    model = Entrada
    template_name = 'articuloDetalle.html'
    context_object_name = 'articulo'
  
class EditarArticulo(UpdateView, LoginRequiredMixin):
    model = Entrada
    form_class = FormularioEdicionArticulo
    template_name= 'articuloEdicion.html'    

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(autor=self.request.user) 
    def get_success_url(self):
        return reverse_lazy("verArticulos")    

class BorrarArticulo(LoginRequiredMixin, DeleteView):
    model = Entrada
    template_name = 'borrarArticulo.html'  
     

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(autor=self.request.user)
    def get_success_url(self):
        return reverse_lazy("verArticulos")  
    
class SobreMi(TemplateView):
    template_name = 'sobreMi.html' 