from modelos.models import Usuario
from django import forms

class UserForm(forms.ModelForm):
    contrasenha = forms.CharField(widget=forms.PasswordInput())
    id_usuario = forms.HiddenInput(id(Usuario))

    class Meta:
        model = Usuario
        fields = ('id_usuario','username', 'nombre', 'apellido', 'ci', 'telefono', 'contrasenha')
