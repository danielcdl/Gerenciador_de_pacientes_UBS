from django.contrib import admin
from django.urls import path, include

from .views import Index

app_name = 'home'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('pacientes/', include('pacientes.urls', namespace='pacientes')),
]
