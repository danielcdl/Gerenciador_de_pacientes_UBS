from django.urls import path, re_path

from .views import Index, Agendar, Calendario, Agendados
from pacientes.views import autocomplete_pacientes, consultar_paciente

app_name = 'agendamento'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    re_path(r'^calendario/(?P<profissional>[a-z]{3})/((?P<mes>[\d]{2})-(?P<ano>[\d]{4})/)?$', Calendario.as_view(), name='calendario'),
    re_path(
        r'^agendar/(<profissional>[a-z]{3})/(<data>[\d]{2}[-][\d]{2}[-][\d]{4})/(<turno>[MT])/$',
        Agendar.as_view(), name='agendar'),
re_path(r'^agendados/(?P<profissional>[a-z]{3})/$',
        Agendados.as_view(), name='agendados'),
]
