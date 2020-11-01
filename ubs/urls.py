from django.contrib import admin
from django.urls import path, include

app_name = 'ubs'

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('pacientes/', include('pacientes.urls', namespace='pacientes')),
    path('agendamento/', include('agendamento.urls', namespace='agendamento')),
    path('admin/', admin.site.urls),
]
