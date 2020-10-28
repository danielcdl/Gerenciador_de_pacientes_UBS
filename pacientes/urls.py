from django.urls import path

from .views import Consultar, Cadastro, tabela_busca

app_name = 'pacientes'

urlpatterns = [
    path('consultar/', Consultar.as_view(), name='consultar'),
    path('consultar/tabela/', tabela_busca, name='consultar'),
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
]
