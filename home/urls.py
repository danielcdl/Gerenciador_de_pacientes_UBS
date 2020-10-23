from django.contrib import admin
from django.urls import path, include

from .views import index

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
]
