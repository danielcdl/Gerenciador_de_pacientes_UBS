from django.urls import path

from .views import Consultar, Cadastro, consultar_paciente

app_name = 'pacientes'

urlpatterns = [
    path('consultar/', Consultar.as_view(), name='consultar'),
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
    path('cadastro/dados/', consultar_paciente, name='dados'),
]
