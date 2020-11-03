from django.urls import path

from .views import Agendar, calendario
from pacientes.views import autocomplete_pacientes, consultar_paciente

app_name = 'agendamento'

urlpatterns = [
    path('', Agendar.as_view(), name='agendar'),
    path('calendario/', calendario, name='calendario'),
    path('autocomplete/', autocomplete_pacientes, name='autocomplete'),
    path('busca/', consultar_paciente, name='busca'),
]
