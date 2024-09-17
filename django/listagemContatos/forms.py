from django import forms
from listagemContatos.models import Cadastro

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ['nome', 'email', 'senha']
        widgets = {'senha': forms.PasswordInput()}