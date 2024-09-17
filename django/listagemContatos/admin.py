from django.contrib import admin
from listagemContatos.models import Cadastro

# Register your models here.

@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'data']
    search_fields = ['nome', 'email']
    list_filter = ['data']