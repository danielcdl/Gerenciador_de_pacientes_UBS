from django.urls import path

from .views import Agendamento

app_name = 'agendamento'

urlpatterns = [
    path('', Agendamento.as_view(), name='agendamento'),
]
