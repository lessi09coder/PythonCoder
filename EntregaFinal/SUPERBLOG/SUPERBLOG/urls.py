"""
URL configuration for SUPERBLOG project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AlexBlog.views import Home, LoginUser, LogoutUser, RegistroUsuarios, AgregarArticulos, VerArticulos, ArticuloDetalle
#luego borrar este:
from AlexBlog import views



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Home.as_view(), name = 'home'),
    path("login/", LoginUser.as_view() , name= 'login'),
    path("logout/", LogoutUser.as_view(), name= 'logout'),
    path("registro/", RegistroUsuarios.as_view(), name= 'registro'),
    path("agregarArticulos/", AgregarArticulos.as_view(), name= 'agregarArticulos'),   
    path("todosArticulos/", VerArticulos.as_view(), name= 'verArticulos'), 
    path('todosArticulos/articulo/<int:pk>/', ArticuloDetalle.as_view(), name='articuloDetalle'),
]


#path("registro/", views.registro, name= 'registro'),
#path("agregarArticulos/", views.agregarArticulos, name= 'agregarArticulos'),  