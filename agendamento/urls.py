from django.urls import path, re_path

from .views import Index, Agendar, Calendario, Agendados

app_name = 'agendamento'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    re_path(r'^calendario/(?P<profissional>[a-z]{3})/(?P<mes>[\d]{1,2})-(?P<ano>[\d]{4})/$', Calendario.as_view(), name='calendario'),
    re_path(
        r'^agendar/(?P<profissional>[a-z]{3})/(?P<data>\d{2}-\d{2}-\d{4})/(?P<turno>[MT])/$',
        Agendar.as_view(), name='agendar'),
    re_path(r'^agendados/(?P<profissional>[a-z]{3})/$', Agendados.as_view(), name='agendados'),
]
