from django.urls import path, re_path

from .views import Consultar
from .views import Cadastro
from .views import CadastroPaciente
from .views import CadastroFamilia
from .views import consultar_paciente
from .views import autocomplete_pacientes
from .views import adicionar_pacientes_xls

app_name = 'pacientes'

urlpatterns = [
    path('consultar/', Consultar.as_view(), name='consultar'),
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
    path('inserir/', adicionar_pacientes_xls, name='inserir'),
    path('cadpaciente/', CadastroPaciente.as_view(), name='cadastro_paciente'),
    path('cadfamilia/', CadastroFamilia.as_view(), name='cadastro_familia'),
    re_path(r'^autocomplete/(?P<nome>[a-zA-Z\s]+)/$', autocomplete_pacientes),
    re_path(r'^(?P<tipo>[a-z]+)/(?P<dado>[\w\s]+)/$', consultar_paciente),
]

