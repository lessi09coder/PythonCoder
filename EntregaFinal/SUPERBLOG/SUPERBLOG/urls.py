from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from AlexBlog.views import (
    Home,
    LoginUser,
    LogoutUser,
    RegistroUsuarios,
    EditarUsuario,
    AgregarArticulos,
    VerArticulos,
    ArticuloDetalle,
    EditarArticulo,
    BorrarArticulo,
    SobreMi,
)

# luego borrar este:
from AlexBlog import views



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Home.as_view(), name="home"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", LogoutUser.as_view(), name="logout"),
    path("registro/", RegistroUsuarios.as_view(), name="registro"),
    path("editarUsuario/", EditarUsuario.as_view(), name="editarUsuario"),    
    path("agregarArticulos/", AgregarArticulos.as_view(), name="agregarArticulos"),
    path("todosArticulos/", VerArticulos.as_view(), name="verArticulos"),
    path(
        "todosArticulos/articulo/<int:pk>/",
        ArticuloDetalle.as_view(),
        name="articuloDetalle",
    ),
    path("todosArticulos/articulo/editarArticulo/<int:pk>/", EditarArticulo.as_view(), name="editarArticulo"),    
    path("todosArticulos/articulo/borrarArticulo/<int:pk>/", BorrarArticulo.as_view(), name="borrarArticulo"), 
    path("about/", SobreMi.as_view(), name="sobreMi"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'AlexBlog.views.error_404'