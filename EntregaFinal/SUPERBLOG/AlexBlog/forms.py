from django import forms
from django.contrib.auth.models import User


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
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            return forms.ValidationError('Las contraseñas no son iguales.')
        return cd['password2']
        
class LoginUsuarios(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)