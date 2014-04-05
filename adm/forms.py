from adm.models import UserProfile
from modelos.models import Usuario
from django import forms

class UserForm(forms.ModelForm):
    contrasenha = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Usuario
        fields = ('username', 'nombre', 'apellido', 'ci', 'telefono', 'contrasenha')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'telefono')