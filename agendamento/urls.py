from django.urls import path

from .views import Agenda, calendario

app_name = 'agendamento'

urlpatterns = [
    path('', Agenda.as_view(), name='agendamento'),
    path('calendario/', calendario, name='calendario'),
]
