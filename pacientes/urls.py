from django.urls import path

from .views import Cadastro

app_name = 'pacientes'

urlpatterns = [
    path('', Cadastro.as_view(), name='cadastro'),
]
