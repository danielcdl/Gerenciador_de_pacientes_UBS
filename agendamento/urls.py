from django.urls import path, re_path

from .views import Index, Agendar, Calendario
from pacientes.views import autocomplete_pacientes, consultar_paciente

app_name = 'agendamento'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    re_path(r'^calendario/(?P<profissional>[a-z]{3})/$', Calendario.as_view(), name='calendario_atual'),
    re_path(r'^calendario/(?P<profissional>[a-z]{3})/(?P<mes>[0-9]{2})-(?P<ano>[0-9]{4})/$', Calendario.as_view(),
            name='calendario_mes'),
    re_path(
        r'^agendar/(?P<profissional>[a-z]{3})/(?P<data>[0-3][0-9][-][0-1][0-9][-][0-9]{4})/(?P<turno>[MT])/$',
        Agendar.as_view(), name='agendar'),

]
