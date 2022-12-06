from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^lista_pessoas/', lista_pessoas, name='lista_pessoas'),
    re_path(r'^cadastro_pessoas/', cadastro, name='cadastro'),
    re_path(r'^editar_cadastro/(?P<pk>[0-9]+)', editar_cadastro, name='editar_cadastro'),
    re_path(r'^remover_pessoa/(?P<pk>[0-9]+)', remover_pessoa, name='remover_pessoa'),
    re_path(r'^login/', login_user, name='login'),
    re_path(r'^logout', logout_user, name='logout'),
]