from django import forms
#from django.forms import ModelForm
from django.contrib.auth.models import User
from AlexBlog.models import Entrada


#es forms.ModelForm? o es UserCreationForm
class FormularioRegistroUsuario(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20, label='Nombre')
    last_name = forms.CharField(max_length=20, label='Apellido')
    password1 = forms.CharField(widget=forms.PasswordInput, label= "Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, label= "Repetir Contraseña") 
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2 :
            raise forms.ValidationError("Las contraseñas no son iguales")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.set_password(self.cleaned_data['password2'])
            user.save()
        return user
    
      
    
class AgregarArticulos(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
        
        
        #widgets = {'autor': forms.TextInput(attrs={'class': 'form-control', 'value': '' , })}
        #autor viene del model    y falta imagen    
    
    
    
    """  titulo = forms.CharField(max_length=50,label='Titulo')
    subtitulo = forms.CharField(max_length=50,label='Subtitulo')
    cuerpo = forms.CharField(max_length=400, label='Escriba aquí su articulo')
    imagen = forms.URLField(label='Imagen a mostrar')      """  