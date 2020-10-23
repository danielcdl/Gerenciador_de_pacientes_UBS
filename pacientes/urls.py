from django.urls import path

from .views import pacientes

app_name = 'pacientes'

urlpatterns = [
    path('', pacientes, name='index'),
]
