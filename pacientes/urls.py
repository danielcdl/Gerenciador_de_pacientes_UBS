from django.urls import path

from .views import Consultar
from .views import Cadastro
from .views import CadastroPaciente
from .views import CadastroFamilia
from .views import consultar_paciente

app_name = 'pacientes'

urlpatterns = [
    path('consultar/', Consultar.as_view(), name='consultar'),
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
    path('cadpaciente/', CadastroPaciente.as_view(), name='cadastro_paciente'),
    path('cadfamilia/', CadastroFamilia.as_view(), name='cadastro_familia'),
    path('cadpaciente/dados/', consultar_paciente),
    path('cadfamilia/dados/', consultar_paciente),
]
