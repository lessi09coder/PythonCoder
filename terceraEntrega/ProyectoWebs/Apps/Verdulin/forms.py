from django import forms
from .models import Producto

class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto # El modelo del producto
        fields = ['nombre', 'precio', 'cantidad']